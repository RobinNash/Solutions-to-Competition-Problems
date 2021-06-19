//CCC Attack Of The Cipher Texts 06 S2
//July 16, 2019
//By Robin Nash

#include<iostream>
#include<map>
#include<string>

using namespace std;

int main(){
	
	string text, encrypted, cipher;

	getline(cin, text);
	getline(cin, encrypted);
	getline(cin, cipher);
	/*
	text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG";
	encrypted = "UIFARVJDLACSPXOAGPYAKVNQTAPWFSAUIFAMB ZAEPH";
	cipher = "XFABSFAWFSZACBEAQFPQMFAEPJOHAWFSZACBEAUIJOHTAIBAIB";
	*/
	map<char, char> code;
	
	
	for (char ch : "ABCDEFGHIJKLMNOPQRSTUVWXYZ "){
		code[ch] = '.';
	}
	
	for (int i = 0; i<encrypted.length() and i < text.length(); i++){
		char a = text.at(i);
		char b = encrypted.at(i);
		code[b] = a;
	}
	
	for (char ch : cipher){
		char a = code[ch];
		//ct << a;
		printf("%c", a);
	}
	

	
	return 0;
}
//1563310812.0