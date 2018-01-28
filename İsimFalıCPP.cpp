



#include <iostream>
#include <vector>
#include <stdio.h>
#define MAX_N 100000

using namespace std;

long long int N;
long long int maxim = 0;
// A utility function to find factorial of n
long long int fact(long long int n)
{
	return (n <= 1) ? 1 : n * fact(n - 1);
}

// Construct a count array where value at every index
// contains count of smaller characters in whole string
void populateAndIncreaseCount(long long int* count, vector<long long int> strX)
{
	long long int i;

	for (i = 0; i<N; ++i)
		++count[strX[i]];

	for (i = 1; i < maxim; ++i)
		count[i] += count[i - 1];
}

// Removes a character ch from count[] array
// constructed by populateAndIncreaseCount()
void updatecount(long long int* count, char ch)
{
	long long int i;
	for (i = ch; i < maxim; ++i)
		--count[i];
}

// A function to find rank of a string in all permutations
// of characters
long long int findRank(vector<long long int> strX)
{
	long long int len = strX.size();
	long long int mul = fact(len);
	long long int rank = 1, i;
	maxim = len;
	// all elements of count[] are initialized with 0
	long long int count[MAX_N] = { 0 };

	// Populate the count array such that count[i] 
	// contains count of characters which are present
	// in strX and are smaller than i
	populateAndIncreaseCount(count, strX);

	for (i = 0; i < len; ++i)
	{
		mul /= len - i;

		// count number of chars smaller than strX[i]
		// fron strX[i+1] to strX[len-1]
		rank += count[strX[i] - 1] * mul;

		// Reduce count of characters greater than strX[i]
		updatecount(count, strX[i]);
	}

	if (rank % 2 == 1) {
		cout << "NO\n";
	}
	else
	cout << "YES\n";

	return rank;
}


vector<long long int>  permute(vector<long long int> arr, vector<long long int>perx) {
	
	vector<long long int> temp(N,0);
	for (long long int i = 0; i < N; i++)
	{
		temp[perx[i] - 1] = arr[i];
	}

	return temp;
}

 int main() {

	long long int Q,  K ;
	cin >> Q >> N >> K;

	vector<long long int> per;
	long long int read;
	for (long long int s = 0; s < N; s++) {

		cin >> read;
		per.push_back(read);
	}


	vector<vector<long long int>>sayilar;




	for (long long int i = 0; i < Q; i++)
	{
		vector<long long int> sira;
		

		for (long long int i = 0; i < N; i++)
		{
			cin >> read;
			sira.push_back(read);
		}
		sayilar.push_back(sira);
		sira.clear();
	}


	vector<long long int> mPerm(N,0);
	mPerm = per;
	for (long long int i = 0; i < K; i++)
	{
		mPerm = permute(mPerm, per);
	}

	vector<long long int>sP(N, 0);

	for (long long int i = 0; i < Q; i++)
	{
		sP = permute(sayilar[i], mPerm);

		findRank(sP);
	}




	return 0;
}



































