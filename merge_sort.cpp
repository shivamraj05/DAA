#include<iostream>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>

#define max 5000
using namespace std;
void merge(int*,int,int*,int,int*,int);
void mergesort(int a[],int n)
{ 
int p=n/2,q=(n-(n/2));
 int b[p];
 int c[q];
	
 if(n>1)
   {
 for(int i=0;i<p;i++)
  {
    b[i]=a[i];
      
  }
 for(int i=0;i<q;i++)
  {
    c[i]=a[i+p];
      
  }

   mergesort(b,p);
   mergesort(c,q);
   

    merge(b,p,c,q,a,n); }
}

void merge(int b[],int p,int c[],int q,int a[],int n)
{
   int i=0,j=0,k=0;
 while(i<p&&j<q)
{
  if(b[i]<=c[j])
    { a[k]=b[i];
      k++; i++;
     }
   else
    {
      a[k]=c[j];
       k++;
       j++;
     }
  }
 if(i==p)
  {
    for(;j<q;j++)
     {
      a[k]=c[j];
      k++;
      }
  }
  if(j==q)
 {
    for(;i<p;i++)
     {
      a[k]=b[i];
      k++;
      }
  }

}


int main()
{
  int a[max],n;

  cout<<"Enter the size of array : ";
  cin>>n;
   srand(time(NULL));
  for(int i=0;i<n;i++)
     a[i]=rand()%500;
    double start=clock();
   mergesort(a,n);
    sleep(10);
    double end=clock();
   double total_time=((double)(end-start))/CLOCKS_PER_SEC;
    cout<<"Sorted Array:\n";
    for(int i=0;i<n;i++)
       cout<<a[i]<<"  ";
    cout<<"\nTotal time:"<<total_time<<endl;
   return 0;
}


