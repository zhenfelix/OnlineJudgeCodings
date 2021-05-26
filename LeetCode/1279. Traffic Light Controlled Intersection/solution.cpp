class TrafficLight {
public:
    TrafficLight()
    {
        
    }

    void carArrived(
        int carId,                   // ID of the car
        int roadId,                  // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        int direction,               // Direction of the car
        function<void()> turnGreen,  // Use turnGreen() to turn light to green on current road
        function<void()> crossCar    // Use crossCar() to make car cross the intersection
    ) {
        lock_guard<mutex> lk(my_mutex);
        if (greenA ^ (roadId == 1)){
            turnGreen();
            greenA = !greenA;
        }
            
        crossCar();
    
    }
private: 
    mutex my_mutex;
    bool greenA = true;
};

// class TrafficLight {
// public:
//     TrafficLight()
//         :greenRoad(1)
//     {
        
//     }

//     void carArrived(
//         int carId,                   // ID of the car
//         int roadId,                  // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
//         int direction,               // Direction of the car
//         function<void()> turnGreen,  // Use turnGreen() to turn light to green on current road
//         function<void()> crossCar    // Use crossCar() to make car cross the intersection
//     ) {
//         lock_guard<mutex> lk(my_mutex);
//         if (greenRoad != roadId){
//             turnGreen();
//             greenRoad = roadId;
//         }
            
//         crossCar();
    
//     }
// private: 
//     mutex my_mutex;
//     int greenRoad;
// };
