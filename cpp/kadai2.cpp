#include<cstring>
#include<iostream>
#include<string>

using namespace std;


struct car{
    int volume;
    int price;
    double gas;
    char type[2];
};

void showCar(struct car *ad){
    cout<<"----------------------"<<endl;
    cout<<ad->volume<<endl;
    cout<<ad->price<<endl;
    cout<<ad->gas<<endl;
    cout<<ad->type<<endl;
    cout<<"----------------------"<<endl;
}


int main(){
    struct car jeep;
    struct car crown;
    struct car GTR;

    jeep.volume=2000;
    jeep.price=500;
    jeep.gas=15.5;
    strcpy(jeep.type,"NA");

    crown.volume=2000;
    crown.price=740;
    crown.gas=17.0;
    strcpy(crown.type,"HV");

    GTR.volume=3800;
    GTR.price=1282;
    GTR.gas=7.24;
    strcpy(GTR.type,"NA");
    
    //string carname;
    int carnumber;

    while(1){
        cout<<"please input car nunber"<<endl;
        cout << "1:jeep" << endl;
        cout << "2:crown" << endl;
        cout << "3:GTR" << endl;
        cout<<"0:end"<<endl;
        cin >> carnumber;
        switch (carnumber)
        {
        //case　"jeep":
        case 1:
            showCar(&jeep);
            break;
        //case "crown":
        case 2:
            showCar(&crown);
            break;
        //case "GTR":
        case 3:
            showCar(&GTR);
            break;
        case 0:

        default:
            break;
        }
        if(carnumber==0)break;
    }
    return 0;
}

