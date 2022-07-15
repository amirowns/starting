//create an object
let dog = {
  name: "Donald",
  numLegs: 4,
  //add a method to the object
  sayLegs: function () {
    return "This dog has " + this.numLegs + " legs.";
  },
};

//print properties of the object
console.log(dog.name);
console.log(dog.numLegs);
console.log(dog.sayLegs());

//constructors
function Dog() {
  this.name = "Albert";
  this.color = "red";
  this.numLegs = 2;
}
//create new object
let hound = new Dog();

//constructors accepting variables
function Hog(name, color) {
  this.name = name;
  this.color = color;
  this.numLegs = 4;
}
// create new object and pass variables
let terrier = new Hog("bobby", "pink");

// instanceOf returns True/False if it is an instance of the constructor
function House(numBedrooms) {
  this.numBedrooms = numBedrooms;
}
let myHouse = new House(6);

myHouse instanceof House;

//Own properties are defined directly on the instance variable
function Bird(name) {
  this.name = name;
  this.numLegs = 2;
}

let canary = new Bird("Tweety");
let ownProps = [];

for (let property in canary) {
  if (canary.hasOwnProperty(property)) {
    ownProps.push(property);
  }
}

console.log(ownProps);

//prototype properties are defined on the entire prototype
function Bog(name) {
  this.name = name;
}
// add numLegs to EVERY instance of Bog
Bog.prototype.numLegs = 2;

let beagle = new Bog("Snoopy");
let ownPropss = [];
let prototypeProps = [];

console.log(beagle.numLegs);

//makes a list of the Own properties and then a list of the prototype properties
for (let property in beagle) {
  if (beagle.hasOwnProperty(property)) {
    ownPropss.push(property);
  } else {
    prototypeProps.push(property);
  }
}

console.log(ownPropss);
console.log(prototypeProps);

// the .constructor property, generally better to use instanceof method
console.log(hound.constructor === Dog);

// more efficient way to set prototype to new object instead of Dog.prototype.eat = function()...
Dog.prototype = {
  //remember to define the constructor property, otherwise it can be overwritten
  constructor: Dog,
  eat: function () {
    console.log("nom nom nom");
  },
  describe: function () {
    console.log("my name is " + this.name);
  },
};

//basically same as instanceof ??? returns True/False
Dog.prototype.isPrototypeOf(hound);

//prototype is a prototype....... of Object
Object.prototype.isPrototypeOf(Dog.prototype);

function Animal() {}

//can make this supertype so you can remove it from subclasses
Animal.prototype = {
  constructor: Animal,
  describe: function () {
    console.log("my name is " + this.name);
  },
};

//better for some reason than using let animal = new Animal();
let animal = Object.create(Animal.prototype);

//make new "class" and set it to use the Animal prototype
function Birdie() {}
Birdie.prototype = Object.create(Animal.prototype);

let duck = new Birdie("John");
duck.describe(); // has the Animal methods

//needed to fix the constructor properties
Birdie.prototype.constructor = Birdie;
duck.constructor;

//add method to prototype
Birdie.prototype.fly = function () {
  console.log("I'm flying!");
};
