import 'dart:io';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:open_file/open_file.dart';

void main() {
  runApp(const Meketa());
}

//dir is a string where the selected directory(folder)'s path
String flashDriveDirectory = "";
String current = Directory.current.path;
File succesful = File("$current\\drive_path.txt");

class Meketa extends StatefulWidget {
  const Meketa({super.key});

  @override
  State<Meketa> createState() => _MeketaState();
}

class _MeketaState extends State<Meketa> {
  @override
  Widget build(BuildContext context) {
    double windowWidth = MediaQuery.of(context).size.width;
    double windowHeight = MediaQuery.of(context).size.height;
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Center(
          child: Container(
            height: windowHeight * 0.8,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  padding: const EdgeInsets.only(bottom: 50),
                  width: 280,
                  child: Image.asset("assets/images/usb-drive.png"),
                ),
                Padding(
                  padding: const EdgeInsets.only(top: 20),
                  child: ElevatedButton(
                      style: ButtonStyle(
                          side: MaterialStateProperty.all(
                              BorderSide(width: 1, color: Colors.black)),
                          minimumSize: MaterialStateProperty.all(Size(120, 50)),
                          foregroundColor:
                              MaterialStateProperty.all(Colors.black)),
                      onPressed: () async {
                        String? result =
                            await FilePicker.platform.getDirectoryPath();
                        if (result != null) {
                          flashDriveDirectory = result;
                        }
                      },
                      child: Text("Choose Folder")),
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
// class MyApp extends StatefulWidget {
//   const MyApp({super.key});

//   @override
//   State<MyApp> createState() => _MyAppState();
// }

// class _MyAppState extends State<MyApp> {
//   // This widget is the root of your application.
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       home: Scaffold(
//           body: Column(
//         children: [
//           const SizedBox(
//             height: 50,
//           ),
//           Row(
//             children: [
//               const SizedBox(
//                 width: 50,
//               ),
//               //this is the selection button. it will change the value of the dir based on the path of the folder you have selected
//               ElevatedButton(
//                   onPressed: () async {
//                     succesful.writeAsString("");
//                     String? result =
//                         await FilePicker.platform.getDirectoryPath();
//                     if (result != null) {
//                       setState(() {
//                         flashDriveDirectory = result;
//                       });
//                       succesful.writeAsString(flashDriveDirectory);
//                     }
//                   },
//                   child: const Text("SELECT FOLDER (flash drive)")),
//               const SizedBox(width: 34),
//               //this is shown on the application as the black box. on this box the selected file path is printed on it.
//               Container(
//                 height: 37,
//                 width: 200,
//                 decoration:
//                     BoxDecoration(border: Border.all(color: Colors.black)),
//                 child: Text(
//                   flashDriveDirectory,
//                   style: const TextStyle(fontSize: 30),
//                 ),
//               ),
//               SizedBox(width: 67),
//             ],
//           ),
//           SizedBox(height: 300),
//           //the two green and red buttons that are found at the bottom are contained in this row.
//           Row(
//             mainAxisAlignment: MainAxisAlignment.spaceAround,
//             children: [
//               //THIS BUTTON THAT WILL APPROVE OUR FLASH DRIVE TO BE USED IN A PROJECTOR
//               ElevatedButton(
//                   style: ElevatedButton.styleFrom(
//                       backgroundColor: Color.fromARGB(255, 59, 255, 66),
//                       minimumSize: Size(179, 50)),
//                   onPressed: () async {
//                     OpenFile.open("./copypath.bat");
//                   },
//                   child: Text("APPROVE")),
//               //this button willl disapprove the flash drive in this case the flash drive data that allows the flash drive to work on the projectors is deleted
//               ElevatedButton(
//                   style: ElevatedButton.styleFrom(
//                       backgroundColor: Color.fromARGB(255, 255, 10, 10),
//                       minimumSize: Size(179, 50)),
//                   onPressed: () {
//                     OpenFile.open("./disapprove.bat");
//                   },
//                   child: Text("DISAPPROVE"))
//             ],
//           )
//         ],
//       )),
//     );
//   }
// }
