# ArchiCAD fix

## Persistent crashing or freezing

Use the Registry Cleaner (Windows) or Preferences Cleaner (macOS) when Archicad shows persistent issues caused by damaged or conflicting preference or registry entries—such as unexpected crashes, missing interface elements, incorrect Work Environment settings, or problems that remain after reinstalling the software. These tools reset Archicad's preference files, allowing you to restore stable operation.

### 1. Preparation steps

Running the Registry or Preferences Cleaner removes all custom Work Environment profiles and DXF/DWG translators from all installed Archicad versions. If you want to keep these settings, export or back them up before continuing.
The files can be found in the following locations:

```
~/Library/Application Support/Graphisoft/DXF-DWG Translators 29.0.0 USA
~/Library/Preferences/Graphisoft/AC29.0.0 USA v1/WorkEnvironment
```

Notes:
* Folder names may differ depending on the installed Archicad version.
* The Registry/Preferences Cleaner removes preference files for all installed Archicad versions.
* If you are working on a Teamwork project, perform Send & Receive, save the project, and close it before running the cleaner.
* Do not install or run the Registry Cleaner on a BIMcloud server machine. Doing so removes all Graphisoft product preferences and requires a full reconfiguration of BIMcloud.
* After running the cleaner, you will need to sign in again with your Graphisoft ID.

### 2. Running the Registry or Preferences Cleaner

1. Download the required file: [Preferences Cleaner](https://pub.graphisoft.de/gsmucftp/PUB//DownloadDateien/cleaner/GSPreferencesCleaner_Mac.zip)
2. Save and close all instances of Archicad.
3. Run the Cleaner app.
   * Locate the 'GS Preference Cleaner.app' and Right-click > Open.
   * If you get the following error message, don't click on anything yet.

     ![](ArchiCAD%20fix/41764853872657.png)

   * Go to System Settings > Privacy & Security and scroll down to the 'Security' section at the bottom.
   * You will see a message that states: "GS Preferences Cleaner.app" was blocked to protect your Mac.
   * Click on the 'Open Anyway' button.

     ![](ArchiCAD%20fix/41764869907345.png)

   * A new window will pop up, click 'Open Anyway'.

     ![](ArchiCAD%20fix/41764853875729.png)

4. The Graphisoft Preferences Cleaner window will appear. Click the Clean button.

   ![](ArchiCAD%20fix/41764778329105.png)

5. After the process completes, reopen Archicad and check whether the issue has been resolved.
6. If the issue persists, run the cleaner again and this time remove all checkmarks.

   ![](ArchiCAD%20fix/41763384315409.png)

## Notes

Source: https://support.graphisoft.com/hc/en-us/articles/30685959049233-Archicad-Registry-Cleaner-Windows-and-Preferences-Cleaner-macOS

#groundcontrol #groundcontrol/archicad
