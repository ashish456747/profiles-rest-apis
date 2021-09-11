1.  ViewSet
2. APIView
- Describe logic to make API endpoint
ApiViews
- Uses standard HTTP methods for functions
  get: return one or items
  post: create an item
  put: update an item
  patch: partially update an item
  delete: delete an item
- Give you most control over logic
  perfect for implementing complex logic
  calling other APIs
  working with local files
When to use ApiViews?
- Need full control over the logic
- Processing files and rendering a synchronous response
- You are calling othe APIs/services
- Accessing local files/data
  
