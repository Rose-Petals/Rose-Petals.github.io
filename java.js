/*
let age = 17;
let in_drivers_ed = true;
console.log("Checking age...")
if(age >= 16 && in_drivers_ed)
    {
        console.log("You can get a driver's permint! Yaaay!");
    }
else
    {
        console.log("You cannot get a driver's permit. Bummer T-T");
    }
*/

/*
let grade = "B";

if( grade = "A")
    {
        console.log("You can go to the mall!");
    }
else
    {
        console.log("You cannot go to the mall. Go study!!")
    }
*/

let path = prompt("What path do you take? 1 for Desert, 2 for Beach, or 3 for Woods ")
if (path == 1)
    {
        let desert_choice = prompt("Do you choose to escape the desert (1) or look for water (2) ")
        if (desert_choice ==1)
            console.log("You escape!! Game over");
        else 
        {
            console.log("You die of thirst. Sad :(");
        }
    }
else if (path == 2)
    {
        console.log("You drowned. You dumdum")
    }
else if (path == 3)
    {
        console.log("You found a cabin!")
    }
