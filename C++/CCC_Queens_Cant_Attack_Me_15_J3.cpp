//CCC Queens Cant Attack Me 15 J3
//August 17, 2019
//By Robin Nash

#include<iostream>

using namespace std;


int main(){

	int n, q;
	scanf("%d %d",&n,&q);

	
	int board[n][n];
	
	for (int y=0; y<n; y++){
		for(int x=0;x<n;x++){
			board[y][x] = 1;
		}
	}
	
	for (int i=0; i<q;i++){
		int x,y;
		scanf("%d %d",&y,&x);
		x --;
		y --;


		for (int i=0; i<n; i++){
			//Verticle
			board[i][x] = 0;
			
			//Horizontal
			board[y][i] = 0;
			
			//Quad 1
			if (x+i < n && y-i >=0) 
				board[y-i][x+i] = 0;
			
			//Quad 2
			if (x-i >= 0 && y-i >=0) 
				board[y-i][x-i] = 0;
			
			//Quad 3
			if (x-i >= 0 && y+i < n) 
				board[y+i][x-i] = 0;
			
			//Quad 4
			if (x+i < n && y+i < n) 
				board[y+i][x+i] = 0;	
			
		}	
	}
	
	
	
	int total = 0;
	for (int y=0; y<n; y++){
		for(int x=0;x<n;x++){
			total += board[y][x];
		}
	}
	
	printf("%d",total);
	
		
	return 0;
}

//1566072134.0