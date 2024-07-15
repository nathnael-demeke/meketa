#include <stdio.h>
#include <winsock2.h>
#include <WS2tcpip.h>
#include <stdlib.h>
#include <process.h>
#define true 1
#include "cJSON/cJSON.h"

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

      if (strcmp(action_string,"Approve")) {
         system("");
      }

      else {
         printf(action_string);
      }

      closesocket(acceptSocket);
   }
}
