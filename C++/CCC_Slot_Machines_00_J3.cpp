//CCC Slot Machines 00 J3
//August 30, 2019
//By Robin Nash

#include<iostream>

using namespace std;


int main(){
	
	int q,a,b,c;
	scanf("%d", &q);
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	
	int m = 1;
	int plays = 0;
	while (q > 0){
		plays++;
		q--;
		if (m == 1){
			a++;
			if (a % 35 == 0)
				q += 30;
			m = 2;
		}
		else if (m == 2){
			b++;
			if (b % 100 == 0)
				q += 60;
			m = 3;
		}		
		else if (m == 3){
			c++;
			if (c % 10 == 0)
				q += 9;
			m = 1;
		}		
	}
	
	printf("Martha plays %d times before going broke.", plays);

		
	return 0;
}

//1567188640.0