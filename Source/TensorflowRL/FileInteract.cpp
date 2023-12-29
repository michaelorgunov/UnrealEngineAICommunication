//https://www.youtube.com/watch?v=zuJ2tjZW770
//https://www.youtube.com/watch?v=-C0Oljfdizk

#include "FileInteract.h"
#include <Runtime\Core\Public\Misc\Paths.h>
#include <Runtime\Core\Public\HAL\PlatformFileManager.h>

FString UFileInteract::LoadFileToString(FString Filename) {
	FString directory = FPaths::ProjectContentDir();
	FString result;
	IPlatformFile& file = FPlatformFileManager::Get().GetPlatformFile();

	if (file.CreateDirectory(*directory)) {
		FString myFile = directory + "/" + Filename;
		FFileHelper::LoadFileToString(result, *myFile);
	}
	return result;
}

FString UFileInteract::LoadStringToFile(FString Filename, FString Message) {
	FString directory = FPaths::ProjectContentDir();
	IPlatformFile& file = FPlatformFileManager::Get().GetPlatformFile();

	if (file.CreateDirectory(*directory)) {
		FString myFile = directory + "/" + Filename;
		//SaveStringArrayToFile()
		FFileHelper::SaveStringToFile(Message, *myFile);
	}
	return Filename;
}

FString UFileInteract::LoadStringArrayToFile(FString Filename, TArray<FString> MessageArray) {
	FString directory = FPaths::ProjectContentDir();
	IPlatformFile& file = FPlatformFileManager::Get().GetPlatformFile();

	if (file.CreateDirectory(*directory)) {
		FString myFile = directory + "/" + Filename;
		FFileHelper::SaveStringArrayToFile(MessageArray, *myFile);
	}
	return Filename;
}