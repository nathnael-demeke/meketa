#include <stdio.h>
#include <winsock2.h>
#include <WS2tcpip.h>
#include <stdlib.h>
#include <process.h>
#define true 1
#include "cJSON/cJSON.h"

void removechar( char str[], char t)
{
    int i,j;
    i = 0;
    while(i<strlen(str))
    {
        if (str[i]==t) 
        { 
            for (j=i; j<strlen(str); j++)
                str[j]=str[j+1];   
        } else i++;
    }
}

char* concat(const char *s1, const char *s2)
{
    char *result = malloc(strlen(s1) + strlen(s2) + 1); 
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}
void sendSuccessMessage(int accept_socket) {
   cJSON *success_json = cJSON_CreateObject();
   cJSON_AddStringToObject(success_json,"StatusCode", "200");
   cJSON_AddStringToObject(success_json,"Msg","Approved flash drive");
   char *response = cJSON_Print(success_json);
   send(accept_socket,response,strlen(response),0);

}
void filepath_parser(char string[]) {
   int last_removed_index = 0;
   char folders[100][100] = malloc(1000);
   int index = 0;
   for (int i = 0; i < strlen(string); i++) {
      if (string[i] == '\\' && last_removed_index < i) {
         // printf("i = %d last = %d \n", last_removed_index , i);
         char folder[100];
         int char_index = 0;
         for (int j = last_removed_index; j <= i; j++) {
            folder[char_index] = string[j];
            char_index++;
         
         }         
         folders[index] = folder;
         last_removed_index = i + 2;
      }
      
     index++;
   }
   
}
void main() {
   
   WSADATA wsaData;
   int wsaerr;
   WORD wVersionRequested = MAKEWORD(2, 2);
   wsaerr = WSAStartup(wVersionRequested, &wsaData);

   if (wsaerr != 0) {
      printf("The Winsock dll not found!");
   }

   int serverSocket;
   serverSocket = socket(AF_INET, SOCK_STREAM, 0);
   const char *opt;
   if (serverSocket < 0) {
      printf("Error at socket()");
      WSACleanup();
   }

   struct sockaddr_in service;
   service.sin_family = AF_INET;
   service.sin_addr.s_addr = INADDR_ANY;
   service.sin_port = htons(132);  

   if (bind(serverSocket, (const struct sockaddr*) &service, sizeof(service))) {
      perror("cannot bind");
      closesocket(serverSocket);
      WSACleanup();
   } 
   if (listen(serverSocket, 1) < 0) {
      printf("listen(): Error listening on socket");
   }
   int socklen = sizeof (service);
   while (true) {
      int acceptSocket;
      if ((acceptSocket = accept(serverSocket,(struct sockaddr*)&service, &socklen)) < 0) {
         printf("accept failed: ");
         WSACleanup();
      }
      char receiveBuffer[1024];
      recv(acceptSocket, receiveBuffer, 200, 0);
      
      cJSON *request = cJSON_Parse(receiveBuffer);
      cJSON *action = cJSON_GetObjectItemCaseSensitive(request,"Action");
      cJSON *driverDirectory = cJSON_GetObjectItemCaseSensitive(request,"DriverDirectory");
      char *action_string = cJSON_Print(action);
      char *driver_directory_string = cJSON_Print(driverDirectory);
      
      removechar(driver_directory_string,'"');
      removechar(action_string, '"');
      filepath_parser(driver_directory_string);
      if (strcmp(action_string,"Approve") == 0) {
         char* command = concat("copy R.file ", driver_directory_string);
         system(command);
         sendSuccessMessage(acceptSocket);
      }

      else if (strcmp(action_string,"Disapprove") == 0) {
         char* command1 = concat("del ", driver_directory_string);
         char* command2 = concat(command1 , "\\R.file");
         system(command2);
         sendSuccessMessage(acceptSocket);
      }

      else {
         printf("action unrecognized %s",action_string);
      }

      closesocket(acceptSocket);
   }
}
