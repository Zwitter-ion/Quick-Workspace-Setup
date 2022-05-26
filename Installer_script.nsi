;-------------------------------------------------------------------------------
; Includes
!include "MUI2.nsh"
!include "LogicLib.nsh"
!include "WinVer.nsh"
!include "x64.nsh"

;-------------------------------------------------------------------------------
; Constants
!define PRODUCT_NAME "Quick Workspace Setup" 
!define PRODUCT_DESCRIPTION "Save a few clicks by using the Quick Workspace Setup"
!define COPYRIGHT "Copyright © 2022 Parth Sareen"
!define PRODUCT_VERSION "1.0.0.0"
!define SETUP_VERSION 1.0.0.0

;-------------------------------------------------------------------------------
; Attributes
Name "Quick Workspace Setup"
OutFile "install.exe"
InstallDir "$PROGRAMFILES\Quick Workspace Setup"
InstallDirRegKey HKCU "Software\QWS\Quick_Workspace_Setup" ""
RequestExecutionLevel admin ; user|highest|admin

;-------------------------------------------------------------------------------
; Version Info
VIProductVersion "${PRODUCT_VERSION}"
VIAddVersionKey "ProductName" "${PRODUCT_NAME}"
VIAddVersionKey "ProductVersion" "${PRODUCT_VERSION}"
VIAddVersionKey "FileDescription" "${PRODUCT_DESCRIPTION}"
VIAddVersionKey "LegalCopyright" "${COPYRIGHT}"
VIAddVersionKey "FileVersion" "${SETUP_VERSION}"

;-------------------------------------------------------------------------------
; Modern UI Appearance
!define MUI_ICON ".\Img\Icon.ico"
!define MUI_UNICON ".\Img\Icon.ico"
!define MUI_HEADERIMAGE_BITMAP ".\Img\hello.bmp"
!define MUI_FINISHPAGE_NOAUTOCLOSE
BrandingText "${PRODUCT_NAME} ${PRODUCT_VERSION}"

;-------------------------------------------------------------------------------
; Installer Pages
!insertmacro MUI_PAGE_LICENSE ".\LICENSE"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

;-------------------------------------------------------------------------------
; Uninstaller Pages
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

;-------------------------------------------------------------------------------
; Languages
!insertmacro MUI_LANGUAGE "English"

;-------------------------------------------------------------------------------
; Installer Sections
Section "Quick Workspace Setup" MyApp
	SetOutPath $INSTDIR
	File /r ".\*"
	CreateDirectory '$SMPROGRAMS\${PRODUCT_NAME}'
	CreateShortCut '$SMPROGRAMS\${PRODUCT_NAME}\Quick Workspace Setup.lnk' '$INSTDIR\Core.exe' '$INSTDIR\Core.exe'
	WriteUninstaller "$INSTDIR\Uninstall.exe"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Quick Workspace Setup" "DisplayName" "${PRODUCT_NAME}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Quick Workspace Setup" "UninstallString" '$INSTDIR\Uninstall.exe'
SectionEnd

;-------------------------------------------------------------------------------
; Uninstaller Sections
Section "Uninstall"
	;Delete /R /REBOOTOK "$INSTDIR\\"
	RMDir /R /REBOOTOK "$INSTDIR"
	DeleteRegKey HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\Quick Workspace Setup"
SectionEnd
