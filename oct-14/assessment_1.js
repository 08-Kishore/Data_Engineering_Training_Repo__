// CRUD OPERATIONS

use("commerce_assessment")


db.products.insertMany([
{
product_id: 101,
product_name: "Ultra Laptop",
category: "Electronics",
brand: "TechPro",
price: 72000,
stock: 12,
available: true,
launch_date: ISODate("2026-01-15"),
colors: ["Black", "Silver"],
specifications: {
ram: "16 GB",
storage: "1 TB SSD",
warranty_years: 2
}
},
{
product_id: 102,
product_name: "Wireless Mouse",
category: "Accessories",
brand: "ClickMax",
price: 1800,
stock: 40,
available: true,
launch_date: ISODate("2026-02-10"),
colors: ["Black", "Blue", "Red"],
specifications: {
wireless: true,
warranty_years: 1
}
},
{
product_id: 103,
product_name: "Office Desk",
category: "Furniture",
brand: "WorkSpace",
price: 14500,
stock: 8,
available: true,
launch_date: ISODate("2025-11-20"),
colors: ["Brown", "Black"],
specifications: {
material: "Wood",
adjustable: false,
warranty_years: 3
}
},
{
product_id: 104,
product_name: "Smart Monitor",
category: "Electronics",
brand: "VisionPlus",
price: 26000,
stock: 5,
available: true,
launch_date: ISODate("2026-03-01"),
colors: ["Black"],
specifications: {
screen_size: "27 inch",
resolution: "4K",
warranty_years: 2
}
},
{
product_id: 105,
product_name: "Gaming Chair",
category: "Furniture",
brand: "SeatPro",
price: 18500,
stock: 0,
available: false,
launch_date: ISODate("2026-01-05"),
colors: ["Black", "Red"],
specifications: {
material: "Leather",
adjustable: true,
warranty_years: 3
}
},
{
product_id: 106,
product_name: "Mechanical Keyboard",
category: "Accessories",
brand: "KeyWorks",
price: 5200,
stock: 18,
available: true,
launch_date: ISODate("2026-04-12"),
colors: ["Black", "White"],
specifications: {
backlit: true,
wireless: false,
warranty_years: 1
}
}
])


db.products.find()


db.products.findOne(
  {
    product_id:103
  }
)


db.products.insertOne({
  product_id:107,
  product_name:"Bluetooth Speaker",
  category:"Electronics",
  brand:"SoundMax",
  price:7500,
  stock:20,
  available:true
})


db.products.insertMany([
  {
    product_id:108,
    product_name:"Phone",
    category:"Electronics",
    brand:"Iqoo",
    price:19000,
    stock:50,
    available:true,
    color:[
      "black",
      "white"
    ]
  },
  {
    product_id:109,
    product_name:"Desk",
    category:"Furniture",
    brand:"Wooden Willow",
    price:12500,
    stock:2,
  }
]
)


db.products.updateOne(
  {product_id:102},
  {$set:{price:2000}}
)


db.products.updateMany(
  {product_id:105},
  {
    $set:{
      stock:20,
      available:true
    }
  }
)


db.products.updateOne(
  {product_id:104},
  {$inc:{
    stock:10
  }}
)


db.products.updateOne(
  {product_id:101},
  {$set:{discount_percent:10}}
)


db.products.updateOne(
  {product_id:101},
  {$unset:{
    discount_percent:""
  }}
)


db.products.deleteOne(
  {product_id:109}
)


db.products.deleteMany(
  {stock:0}
)


db.products.countDocuments(
  {product_id:109}
)


//filtering and query operations

db.products.find(
  {category:"Electronics"}
)


db.products.find(
  {price:{$gt:10000}}
)


db.products.find(
  {price:{$gt:5000,$lt:30000}}
)


db.products.find(
  {stock:{$lt:10}}
)


db.products.find(
  {available:true}
)


db.products.find(
  {available:false}
)


db.products.find(
  { category: { $in: ["Electronics", "Furniture"] } }
)



db.products.find(
  {category:{$nin:["Accessories"]}}
)


db.products.find(
  { price: { $gt: 10000 }, stock: { $gt: 5 } }
)



db.products.find(
  { $or: [ { category: "Electronics" }, { price: { $lt: 5000 } } ] }
)


db.products.find(
  {launch_date:{$gt:ISODate("2026-02-01")}}
)


db.products.find(
  {launch_date:{$gt:ISODate("2026-01-01"),
               $lt:ISODate("2026-03-31")}}
)


//projection and sorting operations

db.products.find(
  {},
  {
    product_id:1,
    price:1,
    _id:0
  }
)


db.products.find(
  {},
  {
    product_name:1,
    category:1,
    stock:1,
    _id:0
  }
)


db.products.find().sort({price:1})


db.products.find().sort({price:-1})


db.products.find().sort({product_name:1})


db.products.find().sort({price:-1}).limit(3)


db.products.find().sort({stock:1}).limit(2)


//ARRAY OPERATIONS

db.products.find(
  {color:"black"}
)

db.products.find(
  {
    color:"black",
    color:"silver"
  }
)


db.products.find(
  {
    color:{$in:["white","blue"]}
  }
)


db.products.updateOne(
  { product_id: 101 },
  { $push: { colors: { $each: ["Black", "Silver"] } } }
)


db.products.updateOne(
  { product_id: 101 },
  { $addToSet: { colors: "Black" } }
)


db.products.updateOne(
  {product_id:102},
  {$pull:{
    colors:"red"
  }}
)



db.products.find(
  { colors: { $type: "array" }, $expr: { $gt: [ { $size: "$colors" }, 1 ] } },
  { product_name: 1, colors: 1, _id: 0 }
)


//Embedded Documents Operations

db.products.find(
   {
     "specifications.warranty_years": 2
   }
 )


 db.products.find(
   {
     "specifications.adjustable": true
   }
 )


 db.products.find(
   {
     "specifications.wireless": true
   }
 )


 db.products.updateOne(
  {product_id:103},
  {
    $set:{
      "specifications.warranty_years":5
    }
  }
)


db.products.updateOne(
  { product_id: 101 },
  { $set: { "specifications.country_of_origin": "India" } }
)

db.products.updateOne(
  { product_id: 102 },
  { $set: { "specifications.country_of_origin": "Japan" } }
)


db.products.find(
  {"specifications.country_of_origin":"India"}
)


//Data type operations

db.products.aggregate([
  { $project: { product_name: 1, price_type: { $type: "$price" } } }
])


db.products.aggregate([
  {$project:{product_name:1,launch_date_type:{$type:"$launch_date"}}}
]
)


db.products.aggregate(
  [
    {$project:{
      product_name:1,
      colors_type:{$type:"$colors"}
    }}
  ]
)


db.products.aggregate(
  [
    {$project:{
      product_name:1,
      specifications_type:{$type:"$specifications"}
    }}
  ]
)


db.products.insertOne({
  product_id:109,
  product_name:"Mouse",
  category:"Accessory",
  brand:"Zebronics",
  price:"25000",
  stock:50,
  available:true
})


db.products.find({
  price:"25000"
})


db.products.updateOne(
  {
    price:"25000"
  },
  {
    $set:{price:25000}
  }
  
)


//Customer Collection

db.createCollection("customers")


db.customers.insertMany([
{
customer_id: 501,
customer_name: "Aditya Rao",
email: "aditya@email.com",
active: true,
address: {
city: "Hyderabad",
state: "Telangana",
pincode: "500081"
},
interests: ["Electronics", "Accessories"]
},
{
customer_id: 502,
customer_name: "Maya Thomas",
email: "maya@email.com",
active: true,
address: {
city: "Chennai",
state: "Tamil Nadu",
pincode: "600028"
},
interests: ["Furniture", "Home"]
},
{
customer_id: 503,
customer_name: "Faisal Ahmed",
email: "faisal@email.com",
active: false,
address: {
city: "Hyderabad",
state: "Telangana",
pincode: "500034"
},
interests: ["Electronics"]
},
{
customer_id: 504,
customer_name: "Nikita Shah",
email: "nikita@email.com",
active: true,
address: {
city: "Mumbai",
state: "Maharashtra",
pincode: "400050"
},
interests: ["Furniture", "Electronics"]
}
])


db.customers.find()


db.customers.find({
  active:true
})


db.customers.find({
  "address.city":"Hyderabad"
})


db.customers.find({
  interests:"Electronics"
})


db.customers.find({
  interests:{
    $all:["Furniture","Electronics"]
  }
})


db.customers.updateOne(
  {
    customer_id:502
  },
  {
    $set:{active:true}
  }
)


db.customers.updateOne(
  {
    customer_id:504
  },
  {
    $set:{"address.city":"Chennai"}
  }
)


db.customers.updateOne(
  {
    customer_id:502
  },
  {
    $push:{interests:"Learning"}
  }
)


//Array of Embedded Documents Operations


db.createCollection("orders")


db.orders.insertMany([
{
order_id: 9001,
customer_id: 501,
order_date: ISODate("2026-09-01"),
        status: "Delivered",
        items: [
            {
                product: "Ultra Laptop",
                quantity: 1,
                price: 72000
            },
            {
                product: "Wireless Mouse",
                quantity: 2,
                price: 2000
            }
        ]
    },
    {
        order_id: 9002,
        customer_id: 502,
        order_date: ISODate("2026-09-03"),
        status: "Processing",
        items: [
            {
                product: "Office Desk",
                quantity: 1,
                price: 14500
            }
        ]
    },
    {
        order_id: 9003,
        customer_id: 503,
        order_date: ISODate("2026-09-05"),
        status: "Delivered",
        items: [
            {
                product: "Smart Monitor",
                quantity: 2,
                price: 26000
            },
            {
                product: "Mechanical Keyboard",
                quantity: 1,
                price: 5200
            }
        ]
    }
])


db.orders.find(
  {
    status:"Delivered"
  }
)


db.orders.find(
  {
    "items.product":"Ultra Laptop"
  }
)


db.orders.find(
  {
    "items.quantity":{$gt:1}
  }
)


db.orders.find(
  {
    "items.product":"Smart Monitor",
    "items.quantity":2
  }
)


db.orders.updateOne({
  order_id:9002
},
        {
          $push:{
            items:{
              product:"Mobile",
              quantity:5,
              price:25000
            }
        }
})


db.orders.updateOne(
  {
    order_id:9002
  },
  {
    $pop:{
      items:-1
    }
  }
)


/*
68. Product can have five colors → Array
Multiple values of the same type (colors) fit naturally in an array.


69. Customer has one residential address → Embedded Document
Address has multiple fields (street, city, zip) but only one instance, so embed it.


70. Order contains multiple products → Array of Embedded Documents
Each product in an order has details (id, quantity, price), so store as array of documents.


71. Product has RAM, storage and processor information → Embedded Document
These are related attributes of one product, so group them in a single embedded document.


72. Customer can have thousands of orders over many years → Separate Collection / Reference
Large, growing many-to-many relationship; better to store orders in a separate collection and reference customer.


73. Product can have millions of customer reviews → Separate Collection / Reference
Reviews scale massively; embedding would make product documents too large, so use a separate collection with references.


74. Employee has first name and last name → Simple Field
Two basic attributes, no need for complex structure.


75. Product has multiple tags → Array
Tags are simple values, multiple per product, so an array is sufficient.

*/


//final questions

db.createCollection("suppliers")

db.suppliers.insertMany([
  {
    supplier_id: 201,
    supplier_name: "TechSource Pvt Ltd",
    city: "Chennai",
    active: true,
    categories: ["Electronics", "Computer Accessories"],
    contact: {
      phone: "9876543210",
      email: "support@techsource.in"
    },
    warehouses: ["Chennai Central", "Coimbatore Hub"],
    registration_date: ISODate("2022-05-10")
  },
  {
    supplier_id: 202,
    supplier_name: "FurniWorld",
    city: "Bangalore",
    active: true,
    categories: ["Furniture", "Home Decor"],
    contact: {
      phone: "9123456780",
      email: "info@furniworld.com"
    },
    warehouses: ["Bangalore North", "Hyderabad South"],
    registration_date: ISODate("2021-11-20")
  },
  {
    supplier_id: 203,
    supplier_name: "AgroFresh Supplies",
    city: "Salem",
    active: false,
    categories: ["Groceries", "Organic Produce"],
    contact: {
      phone: "9988776655",
      email: "sales@agrofresh.in"
    },
    warehouses: ["Salem Main", "Madurai Depot"],
    registration_date: ISODate("2020-03-15")
  },
  {
    supplier_id: 204,
    supplier_name: "StyleWear Distributors",
    city: "Mumbai",
    active: true,
    categories: ["Clothing", "Footwear"],
    contact: {
      phone: "9001122334",
      email: "contact@stylewear.com"
    },
    warehouses: ["Mumbai East", "Pune Central"],
    registration_date: ISODate("2023-01-05")
  },
  {
    supplier_id: 205,
    supplier_name: "KitchenPro Essentials",
    city: "Delhi",
    active: true,
    categories: ["Kitchenware", "Appliances"],
    contact: {
      phone: "9556677889",
      email: "help@kitchenpro.in"
    },
    warehouses: ["Delhi NCR", "Lucknow Storage"],
    registration_date: ISODate("2022-08-18")
  }
])


db.suppliers.find({
  active:true
})


db.suppliers.find({
  city:"Delhi"
})


db.suppliers.find(
  {
    categories:"Electronics"
  }
)


db.suppliers.find(
  {
    registration_date:{$gt:ISODate("2026-01-01")}
  }
)



db.suppliers.updateOne(
  {
    supplier_id:201
  },
  {
    $push:{
      warehouses:"Salem Central"
    }
  }
)


db.suppliers.updateOne(
  {
    supplier_id:202
  },
  {
    $set:{
      active:true
    }
  }
)


db.suppliers.updateOne(
  {
    supplier_id:205
  },
  {
    $pop:{
      categories:-1
    }
  }
)


db.suppliers.find(
  {},
  {
    supplier_name:1,
    city:1,
    _id:0
  }
)


db.suppliers.find().sort({registration_date:1})


/*
85. Explain briefly why you used:
an array for categories,
an embedded document for contact details,
an array for warehouse locations

Array for catagories: because the same supplier hangles different jobs nothing more detail in it.
Array for warehouse: same here because warehouse stores only location .
Embedded document for contact: because it has two fields phone and email and they are related to each other.
*/