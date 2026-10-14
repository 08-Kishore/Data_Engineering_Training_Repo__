db = db.getSiblingDB("food_delivery_assessment");

db.restaurants.insertMany([
{
restaurant_id: 101,
restaurant_name: "Spice Kitchen",
city: "Hyderabad",
cuisine: ["Indian", "Biryani"],
rating: 4.5,
active: true,
contact: {
phone: "9876543210",
email: "spice@email.com"
}
},
{
restaurant_id: 102,
restaurant_name: "Urban Pizza",
city: "Mumbai",
cuisine: ["Italian", "Fast Food"],
rating: 4.2,
active: true,
contact: {
phone: "9988776655",
email: "pizza@email.com"
}
},
{
restaurant_id: 103,
restaurant_name: "Green Bowl",
city: "Bangalore",
cuisine: ["Healthy", "Vegetarian"],
rating: 4.7,
active: true,
contact: {
phone: "9123456780",
email: "green@email.com"
}
},
{
restaurant_id: 104,
restaurant_name: "Burger Point",
city: "Hyderabad",
cuisine: ["Fast Food", "Burgers"],
rating: 3.9,
active: false,
contact: {
phone: "9000011111",
email: "burger@email.com"
}
},
{
restaurant_id: 105,
restaurant_name: "Asian Wok",
city: "Delhi",
cuisine: ["Chinese", "Thai"],
rating: 4.4,
active: true,
contact: {
phone: "9222233333",
email: "wok@email.com"
}
}
  ])


db.restaurants.find()


db.restaurants.find(
  { city: "Hyderabad" }
)


db.restaurants.find(
  { active: true, 
    rating: { $gt: 4.3 } }
)


db.restaurants.insertOne({
  restaurant_id: 110,
  name: "Spice Villa",
  city: "Chennai",
  active: true,
  rating: 4.5,
  cuisines: ["Indian", "Fast Food"],
  contact: { phone: "9876543210",
             email: "info@spicevilla.com" }
})


db.restaurants.updateOne(
  { restaurant_id: 104 },
  { $set: { rating: 4.7 } }
)


db.restaurants.updateOne(
  { restaurant_id: 104 },
  { $set: { active: true } }
)


db.restaurants.deleteOne(
  { restaurant_id: 110 }
)


db.restaurants.find(
  { cuisines: "Fast Food" }
)


db.restaurants.find(
  { cuisines: { $all: ["Italian", "Fast Food"] } }
)


db.restaurants.updateOne(
  { restaurant_id: 102 },
  { $addToSet: { cuisines: "Desserts" } }
)


db.restaurants.updateOne(
  { restaurant_id: 103 },
  { $set: { "contact.email": "newemail@restaurant103.com" } }
)


db.restaurants.find(
  { "contact.phone": { $regex: "^9" } }
)


//Orders collection

db.orders.insertMany([
{
        order_id: 5001,
        restaurant_id: 101,
        customer_name: "Adil",
        order_date: ISODate("2026-09-01"),
        status: "Delivered",
        items: [
            { name: "Chicken Biryani", quantity: 2, price: 320 },
            { name: "Coke", quantity: 2, price: 60 }
        ],
        delivery: {
            city: "Hyderabad",
            fee: 40
        }
    },
    {
        order_id: 5002,
        restaurant_id: 102,
        customer_name: "Megha",
        order_date: ISODate("2026-09-02"),
        status: "Processing",
        items: [
            { name: "Farmhouse Pizza", quantity: 1, price: 550 }
        ],
        delivery: {
            city: "Mumbai",
            fee: 60
        }
    },
    {
        order_id: 5003,
        restaurant_id: 103,
        customer_name: "Kabir",
        order_date: ISODate("2026-09-03"),
        status: "Delivered",
        items: [
            { name: "Protein Bowl", quantity: 2, price: 400 },
            { name: "Juice", quantity: 1, price: 150 }
        ],
        delivery: {
            city: "Bangalore",
            fee: 50
        }
    },
    {
order_id: 5004,
restaurant_id: 101,
customer_name: "Nisha",
order_date: ISODate("2026-09-04"),
status: "Cancelled",
items: [
{ name: "Veg Biryani", quantity: 1, price: 250 }
],
delivery: {
city: "Hyderabad",
fee: 40
}
},
{
order_id: 5005,
restaurant_id: 105,
customer_name: "Rohan",
order_date: ISODate("2026-09-05"),
status: "Delivered",
items: [
{ name: "Thai Curry", quantity: 1, price: 480 },
{ name: "Noodles", quantity: 2, price: 300 }
],
delivery: {
city: "Delhi",
fee: 70
}
}
])


db.orders.find(
  { status: "Delivered" }
)


db.orders.find(
  { order_date: { $gt: ISODate("2026-09-02") } }
)


db.orders.find(
  { status: "Delivered", city: "Hyderabad" }
)


db.orders.find(
  { "items.product": "Noodles" }
)


db.orders.find(
  { "items.quantity": { $gt: 1 } }
)


db.orders.find(
  { items: { $elemMatch: { product: "Chicken Biryani", quantity: 2 } } }
)


db.orders.updateOne(
  { order_id: 5002 },
  { $push: { items: { product: "Ice Cream", quantity: 3, price: 150 } } }
)


db.orders.updateOne(
  { order_id: 5002 },
  { $set: { status: "Delivered" } }
)


db.restaurants.find(
  {},
  {
    restaurant_name:1,
    city:1,
    rating:1,
    _id:0
  }
)


db.restaurants.find().sort({rating:-1})


db.restaurants.find().sort({rating:-1}).limit(3)

//Data types

db.restaurants.find(
  {
    rating:{$type:"number"}
  }
)


db.orders.aggregate([
  {$project:{
    order_date_type:{$type:"$order_date"}
  }}
])


db.orders.aggregate([
  {$project:{
    items_type:{$type:"$items"}
  }}
])


db.restaurants.insertOne({
  restaurant_id: 120,
  name: "Test Bistro",
  city: "Chennai",
  active: true,
  rating: "4.5",  
  cuisines: ["Indian", "Fast Food"],
  contact: { phone: "9876543210", email: "test@bistro.com" },
  order_date: ISODate("2026-09-15")
})


db.restaurants.find(
  { rating: { $type: "string" } },
  { restaurant_id: 1, name: 1, rating: 1, _id: 0 }
)

db.restaurants.updateOne(
  { restaurant_id: 120 },
  { $set: { rating: 4.5 } }   
)


db.restaurants.find(
  { rating: { $type: "number" } },
  { restaurant_id: 1, name: 1, rating: 1, _id: 0 }
)


// Final collection and its operations

db.delivery_partners.insertMany([
  {
    partner_id: 301,
    partner_name: "Ravi Kumar",
    city: "Chennai",
    rating: 4.6,
    active: true,
    vehicle: "Bike",
    skills: ["Fast Delivery", "Customer Service"],
    contact: {
      phone: "9876543210",
      email: "ravi.kumar@deliverypartners.com"
    }
  },
  {
    partner_id: 302,
    partner_name: "Priya Sharma",
    city: "Hyderabad",
    rating: 4.8,
    active: true,
    vehicle: "Scooter",
    skills: ["Food Handling", "Route Optimization"],
    contact: {
      phone: "9123456780",
      email: "priya.sharma@deliverypartners.com"
    }
  },
  {
    partner_id: 303,
    partner_name: "Arun Raj",
    city: "Bangalore",
    rating: 4.2,
    active: false,
    vehicle: "Car",
    skills: ["Bulk Orders", "Time Management"],
    contact: {
      phone: "9988776655",
      email: "arun.raj@deliverypartners.com"
    }
  },
  {
    partner_id: 304,
    partner_name: "Meena Iyer",
    city: "Delhi",
    rating: 4.9,
    active: true,
    vehicle: "Electric Bike",
    skills: ["Eco-Friendly Delivery", "Customer Care"],
    contact: {
      phone: "9556677889",
      email: "meena.iyer@deliverypartners.com"
    }
  }
])


db.delivery_partners.find(
  {
    active:true
  }
)


db.delivery_partners.find(
  {
    rating:{$gt:4}
  }
)


db.delivery_partners.updateOne(
  {
    partner_id:4
  },
  {
    $push:{
      skills:"Bike Taxi"
    }
  }
)


db.delivery_partners.updateOne(
  {
    partner_id:304
  },
  {
    $push:{
      skills:"Bike Taxi"
    }
  }
)


db.delivery_partners.updateOne(
  {
    partner_id:304
  },
  {
    $set:{
      rating:5.1
    }
  }
)


db.delivery_partners.find().sort({rating:-1})
