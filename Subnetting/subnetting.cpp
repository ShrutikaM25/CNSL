#include<bits/stdc++.h>
#include<cstdlib>

using namespace std;


void checkClass(string IP)
{
    cout<<"Class of given IP address: "<<" ";
    int firstOct = IP.find('.');
    string fOct = IP.substr(0,firstOct);

    if(stoi(fOct)>=0 && stoi(fOct)<=127)
    {
        cout<<"Class A"<<endl;
        cout<<"Default subnetMask: 255.0.0.0\n";
    }
    else if(stoi(fOct)>=128 && stoi(fOct)<=191)
    {
        cout<<"Class B"<<endl;
        cout<<"Default subnetMask: 255.255.0.0\n";
    }
    else if(stoi(fOct)>=192 && stoi(fOct)<=224)
    {
        cout<<"Class C"<<endl;
        cout<<"Default subnetMask: 255.255.255.0\n";
    }
    else if(stoi(fOct)>=225 && stoi(fOct)<=239)
    {
        cout<<"Class D"<<endl;
        cout<<"Default subnetMask: not defined\n";
    }
    else if(stoi(fOct)>=240 && stoi(fOct)<=255)
    {
        cout<<"Class E"<<endl;
        cout<<"Default subnetMask: not defined\n";
    }
}
int countBits(int n)
{
int count=0;
while(n)
{
count++;
n=n>>1;
}
return count;
}

void createSubnet(string IP,int n)
{
    int bitToTransfer = ceil((double)(log(n))/log(2.0));

    int subnettedMask = 0;

   
    for(int i=7;i>7-bitToTransfer;i--)
    {
        subnettedMask+=pow(2,i);
    }
    cout<<"SubnettedMask: "<<"255.255.255."<<to_string(subnettedMask);
    int rangeToAdd = pow(2,8-bitToTransfer);
    cout<<endl<<rangeToAdd<<endl;
    int varNum = 0;
    cout<<"\nYour range-->>\n";
    int thirdDot = IP.find_last_of('.');
   

    string threeOct = IP.substr(0,thirdDot);
    int i=0;
    for( i;i<n;i++)
    {
        cout<<threeOct<<"."<<varNum<<" - ";varNum+=rangeToAdd-1;
        cout<<threeOct<<"."<<varNum<<endl;
        varNum++;
    }
    cout<<"Unused subnets:\n";
    for(i;i<pow(2,bitToTransfer);i++)
    {
        cout<<threeOct<<"."<<varNum<<" - ";varNum+=rangeToAdd-1;
        cout<<threeOct<<"."<<varNum<<endl;
        varNum++;
    }
}

int main()
{
    int noSbnet;
    string IP;
    cout<<"Number of subnets to mask: ";
    cin>>noSbnet;

    cout<<"Enter the IP: ";
    cin>>IP;

    checkClass(IP);

    createSubnet(IP,noSbnet);
    cout<<endl;
    cout<<endl;
   
    char cmd[50]= "ping ";
    for(int i=0;i<IP.length();i++)
    {
        cmd[5+i] = IP[i];
    }
    system(cmd);
    return 0;
}