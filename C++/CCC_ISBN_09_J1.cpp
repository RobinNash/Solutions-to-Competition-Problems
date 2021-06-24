//CCC I S B N09 J1
//August 16, 2019
//By Robin Nash

#include<iostream>
#include<vector>

using namespace std;

int main(){
	
	vector<int> numbers {9,7,8,0,9,2,1,4,1,8};
	
	
	for(int i=0;i<3;i++){
		int x;
		scanf("%d", &x);
		numbers.push_back(x);
	}
	
	
	int i = 1;
	int total = 0;
	
	for(int x : numbers){
		total += x*i;
		i+=2;
		if (i > 3)
			i = 1;
	}
	
	printf("The 1-3-sum is %d", total);

	return 0;
}
//1565997536.0