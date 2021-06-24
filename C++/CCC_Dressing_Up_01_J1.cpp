//CCC Dressing Up 01 J1
//August 16, 2019
//By Robin Nash

#include<iostream>

using namespace std;

int main(){
	
	int h, w;
	scanf("%d", &h);
	w = h*2;
	
	for (int i=0; i<h;i++){
		int bow, spaces;
		if (i > h/2)
			bow = h-i-1;
		else
			bow = i;
		
		bow = bow*2 + 1;
		spaces = w - bow*2;
		
		
		for (int i=0; i<bow;i++){
			printf("%c", '*');
		}
		
		for (int i=0; i<spaces;i++){
			printf("%c", ' ');
		}
		
		for (int i=0; i<bow;i++){
			printf("%c", '*');
		}
		
		cout << endl;
	}
	
	
	
	
	return 0;
}
//1565997598.0