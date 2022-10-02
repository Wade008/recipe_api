# A flask backend for an online recipe application.

## End Point Documentation

### Recipe API Endpoints User registration, login, read, update and delete 

**User registration**  

- Request: POST /auth/register 

Required data: 

```json  
{
    "username":"username",
	"email": "email@mail.com",
	"password":"password",
	"name":"name",
	"phone":"0000000000",
	"dob":"yyyy-mm-dd"
}
```
Expected response:

```json
{
	"user": "username",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY3NjY0NSwianRpIjoiZWIzYTdiNzYtNzJiZi00ODVlLThiM2QtNmU4NGFlNTI3MDMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjUiLCJuYmYiOjE2NjQ2NzY2NDUsImV4cCI6MTY2NDY5MTA0NX0.bU-rHQC418KIVe3cpF5n284nucKSExtu-QUA4yGBpv0"
}

```
Authentication: 

- Password must be a string, greater than or equal to eight characters long.

Sample POST request: 

```/auth/register```

```json
{
	"username":"wade008",
	"email": "wade2@mail.com",
	"password":"123456789",
	"name":"Wade56",
	"phone":"0123456789",
	"dob":"1980-02-12"
	
}
```
Sample response: 

```json  
{
	"user": "wade008",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY3NjY0NSwianRpIjoiZWIzYTdiNzYtNzJiZi00ODVlLThiM2QtNmU4NGFlNTI3MDMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjUiLCJuYmYiOjE2NjQ2NzY2NDUsImV4cCI6MTY2NDY5MTA0NX0.bU-rHQC418KIVe3cpF5n284nucKSExtu-QUA4yGBpv0"
}
```

**User login**  

- Request: POST /auth/user/login

Required data: 

```json  
{
    "username":"username",
	"password":"password",

}
```
Expected response:

```json
{
	"user": "username",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY3NjY0NSwianRpIjoiZWIzYTdiNzYtNzJiZi00ODVlLThiM2QtNmU4NGFlNTI3MDMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjUiLCJuYmYiOjE2NjQ2NzY2NDUsImV4cCI6MTY2NDY5MTA0NX0.bU-rHQC418KIVe3cpF5n284nucKSExtu-QUA4yGBpv0"
}
```
Authentication: 

- Password must match the password in the system.

Sample POST request: 

```/auth/user/login```

```json

{
	"username":"wade008",
	"email": "wade2@mail.com",
}

```
Sample response: 

```json  
{
	"username": "wade008",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDY3NzI4OCwianRpIjoiN2Q5ZDU2NzEtMDM3Yi00YjY5LWJlZDctNDEzODA5YjA3NDkyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjUiLCJuYmYiOjE2NjQ2NzcyODgsImV4cCI6MTY2NDY5MTY4OH0.WUtOCpuyUe6-pdUPoocXQJ14fIz_FA9ld0yvM-YxdMo"
}

```

**User - view current user details**  

- Request: GET /auth/user/view

Required data: 

- Not applicable

Expected response:

```json
{
	"user_id": 0,
	"username": "username",
	"email": "email",
	"password": "hashed password",
	"name": "name",
	"phone": "0000000000",
	"dob": "yyyy-mm-dd"
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the logged-in user can see their details.

Sample GET request: 

```/auth/user/view```

Sample response: 

```json  
{
	"user_id": 5,
	"username": "wade008",
	"email": "wade2@mail.com",
	"password": "$2b$12$ineFN/qlClSi5b2d4jyrPOzngWhYHALpVOwIUHpEzP8QVGGyTqWIO",
	"name": "Wade56",
	"phone": "0123456789",
	"dob": "1980-02-12"
}
```

**User - update details**  

- Request: PUT /auth/user/view

Required data: 

```json  
{
    "username": "username",
	"email": "email@mail.com",
	"password": "password",
	"name": "name",
	"phone": "0000000000",
	"dob": "yyyy-mm-dd"
}
```
Expected response:
- A successful update will return the user information with the updated details

```json
{
	 "username": "username",
	"email": "email@mail.com",
	"password": "hashed password",
	"name": "name",
	"phone": "0000000000",
	"dob": "yyyy-mm-dd"
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the logged-in user can see their details.

Sample PUT request: 

```/auth/user/view```

```json

{
	"username": "wade008",
	"email": "wade2@mail.com",
	"password": "123456789",
	"name": "Wade Doolan",
	"phone": "0123456789",
	"dob": "1980-02-12"
}

```
Sample response: 

```json  
{
	"user_id": 5,
	"username": "wade008",
	"email": "wade2@mail.com",
	"password": "$2b$12$SZHioNf/SRYLsYceVhHGIOqg08FmcFac57Ht.iXPgUjf/x27FpCf2",
	"name": "Wade Doolan",
	"phone": "0123456789",
	"dob": "1980-02-12"
}
```
**User - delete profile**  

- Request: DELETE /auth/user/view

Required data: 

- Not applicable

Expected response:

```json
{
	"success": "User deleted successfully"
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the logged-in user can delete their profile.

### Recipe API Endpoints for recipes read, post, update and delete

**View all recipes**

- Request: GET /recipes/

Required data: 

- Not applicable

Expected response:

```json

[
    {
        "owner": "owner",
        "recipe_id": 0,
        "recipe_name": " name..",
        "serves": 0,
        "instructions": "Instructions...",
        "time_required": 00.0,
        "private": bool,
        "date_added": "yyyy-mm-dd",
        "recipe_category": "category",
        "ingredient_list": [
            {
                "ingredient": "ingredient",
                "ingredient_requirements": "requirements..."
            }, ...
    
        ],
        "ratings": [
            {
                "rated_by": "user",
                "rating": 0,
                "comment": "comment"
            }, ...
        ]
    }, ...
]

```
Authentication: 

- Not required. Anyone can view the recipes in the system that are not marked as private.

Sample GET request: 

```/recipes```

Sample response: 

```json  

[
    {
        "owner": "John Mayer",
        "recipe_id": 4,
        "recipe_name": " Chicken..",
        "serves": 4,
        "instructions": "Prepare a barbecue for medium-high heat. Coat corn with 2 teaspoons oil. Season with salt and pepper...",
        "time_required": 60.0,
        "private": false,
        "date_added": "2022-09-29",
        "recipe_category": "Chicken",
        "ingredient_list": [
            {
                "ingredient": "Pasta",
                "ingredient_requirements": "250g of pasta"
            },
            {
                "ingredient": "Salt",
                "ingredient_requirements": "1/4 tablespoon of salt"
            }, ...
            
        ],
        "ratings": [
            {
                "rated_by": "Wade Doolan",
                "rating": 5,
                "comment": "Amazing"
            }, ...
            
        ]
    },...
]

```
Query string parameters:

- Parameters: *recipe_name*, *category*
- Required: both parameters are optional, and only one parameter can be used if required
- description: provides a key word search by recipe names and or recipe category containing parameter values.

Sample GET request with parameter:

``` /recipes?recipe_name=chick&category=chick ```

sample response:

```json
[
	{
		"owner": "John Mayer",
		"recipe_id": 4,
		"recipe_name": " Chicken..",
		"serves": 4,
		"instructions": "Prepare a barbecue for medium-high heat. Coat corn with 2 teaspoons oil. Season with salt and pepper...",
		"time_required": 60.0,
		"private": false,
		"date_added": "2022-09-29",
		"recipe_category": "Chicken",
		"ingredient_list": [
			{
				"ingredient": "Pasta",
				"ingredient_requirements": "250g of pasta"
			},...
		],
		"ratings": [
			{
				"rated_by": "Wade Doolan",
				"rating_id": 4,
				"rating": 5,
				"comment": "Amazing"
			},...
		]
	}, ...
	
]
```


**View one recipe**  

- Request: GET /recipes/{recipe_id}

Required data: 

- Not applicable

Expected response:

```json
{
    "owner": "owner",
    "recipe_id": 0,
    "recipe_name": " name..",
    "serves": 0,
    "instructions": "Instructions...",
    "time_required": 00.0,
    "private": bool,
    "date_added": "yyyy-mm-dd",
    "recipe_category": "category",
    "ingredient_list": [
        {
            "ingredient": "ingredient",
            "ingredient_requirements": "requirements..."
        }, ...

    ],
    "ratings": [
        {
            "rated_by": "user",
            "rating": 0,
            "comment": "comment"
        }, ...
    ]
}
```
Authentication: 

- Not required. Anyone can view a recipe in the system that is not marked as private.

Sample GET request: 

```/recipes/1```

Sample response: 

```json  
{
	"owner": "Wade Doolan",
	"recipe_id": 1,
	"recipe_name": "Bacon and Eggs",
	"serves": 2,
	"instructions": "Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
	"time_required": 30.0,
	"private": false,
	"date_added": "2022-09-29",
	"recipe_category": "Breakfast",
	"ingredient_list": [
		{
			"ingredient": "Eggs",
			"ingredient_requirements": "2 eggs"
		},
		{
			"ingredient": "Domestic pig (Piglet, Pork)",
			"ingredient_requirements": "2 bacon rashers"
		}...
	],
	"ratings": [
		{
			"rated_by": "John Mayer",
			"rating": 5,
			"comment": "Wow food"
		},
		{
			"rated_by": "John Mayer",
			"rating": 4,
			"comment": "Love it"
		}...
	]
}
```
**View all recipe for logged-in user**

- Request: GET /recipes/myrecipes

Required data: 

- Not applicable

Expected response:

```json
[
    {
        "owner": "owner",
        "recipe_id": 0,
        "recipe_name": " name..",
        "serves": 0,
        "instructions": "Instructions...",
        "time_required": 00.0,
        "private": bool,
        "date_added": "yyyy-mm-dd",
        "recipe_category": "category",
        "ingredient_list": [
            {
                "ingredient": "ingredient",
                "ingredient_requirements": "requirements..."
            }, ...

        ],
        "ratings": [
            {
                "rated_by": "user",
                "rating": 0,
                "comment": "comment"
            }, ...
        ]
    }, ...

]
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token).

Sample GET request: 

```/recipes/1```

Sample response: 

```json  
{
	"owner": "Wade Doolan",
	"recipe_id": 1,
	"recipe_name": "Bacon and Eggs",
	"serves": 2,
	"instructions": "Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
	"time_required": 30.0,
	"private": false,
	"date_added": "2022-09-29",
	"recipe_category": "Breakfast",
	"ingredient_list": [
		{
			"ingredient": "Eggs",
			"ingredient_requirements": "2 eggs"
		},
		{
			"ingredient": "Domestic pig (Piglet, Pork)",
			"ingredient_requirements": "2 bacon rashers"
		}...
	],
	"ratings": [
		{
			"rated_by": "John Mayer",
			"rating": 5,
			"comment": "Wow food"
		},
		{
			"rated_by": "John Mayer",
			"rating": 4,
			"comment": "Love it"
		}...
	]
}
```
**Post a recipe**

- Request: POST /recipes/

Required data: 

```json
{
	"recipe_name": "name",
	"serves":0,
	"instructions":"instructions...",
	"time_required":0, #in minutes
	"private": bool, #true or false
	"recipe_category": "optional"
}
```

Expected response:

```json
{
	"recipe_name": "name",
	"serves":0,
	"instructions":"instructions...",
	"time_required":0, #in minutes
	"private": bool, #true or false
	"recipe_category": "optional"
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token).

Sample POST request: 

```/recipes```

```json  
{
	"recipe_name": " Chicken..",
	"serves":4,
	"instructions":"Prepare a barbecue for medium-high heat. Coat corn with 2 teaspoons oil. Season with salt and pepper...",
	"time_required":60,
	"private": true,
	"recipe_category": "Chicken"

}
```

Sample response: 

```json  
{
	"owner": "John Mayer",
	"recipe_id": 6,
	"recipe_name": " Chicken..",
	"serves": 4,
	"instructions": "Prepare a barbecue for medium-high heat. Coat corn with 2 teaspoons oil. Season with salt and pepper...",
	"time_required": 60.0,
	"private": true,
	"date_added": "2022-10-02",
	"recipe_category": "Chicken",
	"ingredient_list": [],
	"ratings": []
}
```
**Update a recipe**

- Request: PUT /recipes/{recipe_id}

Required data: 

```json
{
	"recipe_name": "name",
	"serves":0,
	"instructions":"instructions...",
	"time_required":0, #in minutes
	"private": bool, #true or false
	"recipe_category": "optional"
}
```

Expected response:

```json
{
	"recipe_name": "name",
	"serves":0,
	"instructions":"instructions...",
	"time_required":0, #in minutes
	"private": bool, #true or false
	"recipe_category": "optional",
    "ingredient_list": [
		{
			"ingredient": "ingredient",
			"ingredient_requirements": "requirement"
		},...
	],
	"ratings": [
		{
			"rated_by": "user",
			"rating": 0,
			"comment": "comment"
		},...
	]
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token).

Sample PUT request: 

```/recipes/1```

```json  
{
	"recipe_name": "Bacon and Eggs",
	"serves": 2,
	"instructions": "Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
	"time_required": 30.0,
	"private": false,
	"date_added": "2022-09-29",
	"recipe_category": "Breakfast"
	}
```

Sample response: 

```json  
{
	"owner": "Wade Doolan",
	"recipe_id": 1,
	"recipe_name": "Bacon and Eggs",
	"serves": 2,
	"instructions": "Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
	"time_required": 30.0,
	"private": false,
	"date_added": "2022-09-29",
	"recipe_category": "Breakfast",
	"ingredient_list": [
		{
			"ingredient": "Eggs",
			"ingredient_requirements": "2 eggs"
		}, ...
	],
	"ratings": [
		{
			"rated_by": "Wade Doolan",
			"rating": 4,
			"comment": "Lovely food"
		}, ...
	]
}
```
**Delete a recipe**  

- Request: DELETE /recipes/{recipe_id}

Required data: 

- Not applicable

Expected response:

```json
{
	"message": "Recipe successfully deleted from database."
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the recipe owner can delete the recipe. Admin can delete all recipes.

### Recipe API Endpoints for recipe ingredients read, post, update and delete

**View all ingredients for a recipe**

- Request: GET /recipes/{recipe_id}/ingredients 

Required data: 

- Not applicable

Expected response:

```json
[
	{
		"list_id": 0,
		"recipe": "recipe name",
		"ingredient_requirements": "requirements",
		"ingredient": "ingedient"
	}, ...
]
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, any logged-in user can view the recipe ingredients, regardless of ownership.

Sample GET request: 

```/recipes/4/ingredients```

Sample response: 

```json  
[
	{
		"list_id": 15,
		"recipe": " Chicken..",
		"ingredient_requirements": "250g of pasta",
		"ingredient": "Pasta"
	},...
	
]
```
**View one ingredient for a recipe**

- Request: GET /recipes/{recipe_id}/ingredients/{list_id}

Required data: 

- Not applicable

Expected response:

```json
{
    "list_id": 0,
    "recipe": "recipe name",
    "ingredient_requirements": "requirements",
    "ingredient": "ingedient"
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, any logged-in user can view the recipe ingredient, regardless of ownership.

Sample GET request: 

```/recipes/1/ingredients/3```

Sample response: 

```json  
{
	"list_id": 3,
	"recipe": "Bacon and Eggs",
	"ingredient_requirements": "1 tomato",
	"ingredient": "Garden tomato"
}
```
**Post one or more ingredient for a recipe**

- Request: POST /recipes/{recipe_id}/ingredients

Required data: 

```json
[	
    {
        "ingredient": "ingredient",
        "ingredient_requirements": "requirement"
    },
    {
        "ingredient": "ingredient",
        "ingredient_requirements": "requiremwnt"
    }, ...
   
]
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the recipe owner can add ingredients to the recipe. Admin can add ingredients to all recipes.

Sample POST request: 

```/recipes/2/ingredients```

```json
[
    {
        "ingredient": "Garden onion",
        "ingredient_requirements": "Chop half a garden onion"
    }
]
```
Sample response: 

```json  
{
	"message": "Ingredients added to recipe successfully."
}
```
**Update an ingredient for a recipe**

- Request: PUT /recipes/{recipe_id}/ingredients/{list_id}

Required data: 

```json
{
	"ingredient_requirements": "updated requirement",
	"ingredient": "updated ingredient"
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the recipe owner can update an ingredient for the recipe. Admin can update ingredients to all recipes.

Sample PUT request: 

```/recipes/2/ingredients/27```

```json
{
	"ingredient_requirements": "1/4 onion, chopped",
	"ingredient": "Garden Onion"
}
```
Sample response: 

```json  
{
	"list_id": 27,
	"recipe": "Toasted sandwich",
	"ingredient_requirements": "1/4 onion, chopped",
	"ingredient": "Garden onion"
}
```
**Delete an ingredient**  

- Request: DELETE /recipes/{recipe_id}/ingredients/{list_id}

Required data: 

- Not applicable

Expected response:

```json
{
	"message": "Ingredient successfully deleted from database."
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the recipe owner can delete a recipe ingredient. Admin can delete all recipe ingredients.

### Recipe API Endpoints for recipe ratings post and delete

**Post a rating for a recipe** 

- Request: POST /recipes/{recipe_id}/rating

Required data: 

```json
{
	"rating":0,
	"comment":"comment"
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, any logged-in user can post a rating for any non-private recipe.

Sample POST request: 

```/recipes/1/rating```

```json
{
	"rating":5,
	"comment":"Nice"
}
```
Sample response: 

```json  
{
	"owner": "Wade Doolan",
	"recipe_id": 1,
	"recipe_name": "Bacon and Eggs",
	"serves": 2,
	"instructions": "Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
	"time_required": 30.0,
	"private": false,
	"date_added": "2022-09-29",
	"recipe_category": "Breakfast",
	"ingredient_list": [
		{
			"ingredient": "Eggs",
			"ingredient_requirements": "2 eggs"
		},
		{
			"ingredient": "Domestic pig (Piglet, Pork)",
			"ingredient_requirements": "2 bacon rashers"
		},
		{
			"ingredient": "Garden tomato",
			"ingredient_requirements": "1 tomato"
		},
		{
			"ingredient": "Wheat bread",
			"ingredient_requirements": "2 slices"
		}
	],
	"ratings": [
		{
			"rated_by": "John Mayer",
            "rating_id": 8,
			"rating": 5,
			"comment": "Nice"
		}
	]
}
```
**Delete a rating for a recipe**  

- Request: DELETE /recipes/{recipe_id}/rating/{rating_id}

Required data: 

- Not applicable

Expected response:

```json
{
	"message": "Rating successfully removed from the recipe."
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, only the user who posted the rating can remove it. Admin can remove all ratings.

### Recipe API Endpoints for recipe categories read, post, update and delete

**View all categories**

- Request: GET /categories

Required data: 

- Not applicable

Expected response:

```json
[
	{
		"category_id": 1,
		"category": "Breakfast"
	},
	{
		"category_id": 2,
		"category": "Brunch"
	},
	{
		"category_id": 3,
		"category": "Lunch"
	}, ...
]
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, any user can get all categories.

Query string parameters:

- Parameter: *category*
- Required: parameter is optional
- description: provides a key word search for categories containing parameter value.

Sample request with parameter:

``` /categories?category=bread ```

sample response:

```json
[
	{
		"category_id": 30,
		"category": "Bread"
	}
]
```

**View one category**

- Request: GET /categories/{category_id}

Required data: 

- Not applicable

Expected response:

```json
{
    "category_id": 0,
    "category": "category"
    "recipes": [
		{
			"recipe_name": "recipe name",
			"serves": 0,
			"time_required": 0.0,
			"date_added": "yyyy-mm-dd"
		}, ...
	]
}
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, any user can get one category.

Sample GET request: 

```/categories/1```

Sample response: 

```json
{
	"category_id": 1,
	"category": "Breakfast",
	"recipes": [
		{
			"recipe_name": "Bacon and Eggs",
			"serves": 2,
			"time_required": 30.0,
			"date_added": "2022-09-26"
		}
	]
}

```
**Post a new category**

- Request: POST /categories

Required data: 

```json 
{
	"category": "new category"
}
```

Expected response:

```json
{
	"category_id": 0,
	"category": "new category"
}
```
Authentication: 

- An admin user must be logged in with a current JSON Web Token (Bearer Token). Note, only admin users can post new categories.

Sample POST request: 

```/categories/```

```json
{
	"category": "BIG Breakfast"
}
```

Sample response: 

```json
{
	"category_id": 42,
	"category": "BIG Breakfast"
}
```
**Update a category**

- Request: PUT /categories/{category_id}

Required data: 

```json 
{
	"category": "update category"
}
```

Expected response:

```json
{
	"category_id": 0,
	"category": "updated category"
}
```
Authentication: 

- An admin user must be logged in with a current JSON Web Token (Bearer Token). Note, only admin users can update categories.

Sample PUT request: 

```/categories/41```

```json
{
	"category": "BIG BIG Breakfast"
}
```

Sample response: 

```json
{
	"category_id": 42,
	"category": "BIG BIG Breakfast"
}
```

**Delete a category**

- Request: DELETE /categories/{category_id}

Required data: 

- Not applicable

Expected response:

```json
{
	"message": "Category removed successfully"
}
```
Authentication: 

- An admin user must be logged in with a current JSON Web Token (Bearer Token). Note, only admin users can delete categories.

## Recipe API Endpoints for recipe ingredients read

**View all ingredients**

- Request: GET /ingredients

Required data: 

- Not applicable

Expected response:

```json
[
	{
		"ingredient_id": 1,
		"ingredient": "Angelica"
	},
	{
		"ingredient_id": 2,
		"ingredient": "Savoy cabbage"
	},
	{
		"ingredient_id": 3,
		"ingredient": "Silver linden"
	},...
]
```
Authentication: 

- User must be logged in with a current JSON Web Token (Bearer Token). Note, any user can view all ingredients.

Query string parameters:

- Parameter: *ingredient*
- Required: parameter is optional
- description: provides a key word search for ingredients containing parameter value.

Sample request with parameter:

``` /ingredients?ingredient=fish ```

sample response:

```json
[
	{
		"ingredient_id": 296,
		"ingredient": "Atlantic wolffish"
	},
	{
		"ingredient_id": 304,
		"ingredient": "Alaska blackfish"
	},
	{
		"ingredient_id": 308,
		"ingredient": "Bluefish"
	},
	{
		"ingredient_id": 318,
		"ingredient": "American butterfish"
	}...
]
```
