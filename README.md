# How to run server
* pip install -r requirements.txt
* python3 manage.py runserver

# API endpoint: 
By default, the endpoint is localhost:8000/

The following are the APIs that I have created

## api/register/
* Pass username and password in the body to register user
* Example curl command: `curl -X POST http://localhost:8000/api/register/ -d "username=testuser&password=testpassword"`

## api/token/
* Pass username and password to obtain token
* Example curl command: `curl -X POST http://localhost:8000/api/token -d "username=testuser&password=testpassword"`

## api/categories/
* Use token obtained for authorization. API returns a list of all categories. 
* Example curl command: `curl -H "Authorization: Bearer <auth_token>" http://localhost:8000/api/categories/`

## api/tags/
* Use token obtained for authorization. API returns a list of all tags. 
* Example curl command: `curl -H "Authorization: Bearer <auth_token>" http://localhost:8000/api/tags/`

## api/items/
* Use token obtained for authorization. API returns a list of all items. Items can be filtered by passing the following query params: 'sku', 'name', 'category', 'tags', 'stock_status', 'available_stock' 
* Example curl command: `curl -H "Authorization: Bearer <auth_token>" http://localhost:8000/api/items/`
* You can filter items returned by passking 'sku', 'name', 'category', 'tags', 'stock_status', 'available_stock' as query params

## api/items/create
* Use token obtained for authorization. API creates an item in the database. Send post request to create item and pass 'sku', 'name', 'category', 'tags', 'stock_status', 'available_stock' as request body
* Example curl command: `curl -X POST http://localhost:8000/api/items/create/   -H "Content-Type: application/json"   -H "Authorization: Bearer <auth_token>"   -d '{"sku": "SKU003", "name": "Item 3", "category": "Category 1", "tags": ["Tag 1"], "stock_status": "In Stock", "available_stock": 30}'`

## api/categories/create
* Use token obtained for authorization. API creates a category in the database. Send post request to create a category and pass 'name' as request body
* Example curl command: `curl -X POST http://localhost:8000/api/categories/create/   -H "Content-Type: application/json"   -H "Authorization: Bearer <auth_token>"   -d '{"name": "Cat 3"}'`

## api/tags/create
* Use token obtained for authorization. API creates a tag in the database. Send post request to create a tag and pass 'name' as request body
* Example curl command: `curl -X POST http://localhost:8000/api/tags/create/   -H "Content-Type: application/json"   -H "Authorization: Bearer <auth_token>"   -d '{"name": "Tag 3"}'`

# Test Cases
Unit Tests can be found under /api/tests