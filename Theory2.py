

1.1    What does SDLC stand for?
## Software Development Life Cycle



   1.2   What exception is thrown when you divide a number by 0?
## DivideByZeroException



   1.3   What is the git command that moves code from the local repository
            to the remote repository? 
## git push



   1.4   What does NULL represent in a database? 
## the absence or lack of a value in a data field. It’s not the same as an empty string or zero; rather, it signifies the unknown, missing, or undefined state of data




   1.5   Name 2 responsibilities of the Scrum Master 
## 1. Running Scrum Events: The Scrum Master makes sure that all the Scrum events, like daily stand-ups and sprint planning, happen smoothly. They help the team understand why these events are important and keep them on track.

## 2. Clearing the Way: The Scrum Master takes charge of removing any obstacles that could slow down the team. They work closely with everyone involved to solve problems and create a supportive environment. Their goal is to make sure the team can deliver the product without any roadblocks.



   1.6   Name 2 debugging methods, and when you would use them.
## Print Statements: print out variable values or messages at different spots to see what's happening. It's handy to see which part of the code is causing trouble or if you want to keep track of how values change as the program runs.

## Step-by-Step Debugging with a Debugger: a debugger tool lets you go through the code one step at a time. You can set breakpoints, examine variables, and see what's going on at each stage. It's great when dealing with more complex problems or gives a closer look into how your program is running.



   1.7   

## Function called can_pay(price, cash_given) that checks if the cash given is enough to cover the price. It returns True if you can pay, and False if you can't.

## A  situation where this function might throw an error when you call it:

## If you accidentally pass non-number values, like a word or a list, instead of actual numbers for the price or cash_given parameters. When the function tries to compare these non-numeric values using the greater than or equal to (>=) operator, it gets confused and raises a TypeError because it can't do the comparison.

## To handle this error, I would use a try-except block. Inside the try part, you can convert the inputs to numbers using the float() function. If that works, it continues with the comparison. But if a TypeError occurs during the conversion, the code jumps to the except part where you can catch the error and deal with it. In this case, you can simply return False to indicate that the inputs should be numeric.




   1.8    What is git branching? Explain how it is used in Git. 
 ## Allows you to work on different versions of your code at the same time.
## It creates separate paths in your project's timeline, known as branches. You can make changes in a branch without affecting the main codebase. Branching is useful for trying out new ideas, developing features, and fixing bugs in isolation. Once your changes are ready, you can merge the branch back into the main code. Git makes branching easy and helps keep your code organized and collaborative. It allows you to experiment and work on multiple things at once.




   1.9  Design a restaurant ordering system. 
           You do not need to write code, but describe a high-level approach: 


List of Key Requirements:
 ## 1. Interactive Menu Experience: an interactive menu interface that showcases appetising food images, descriptions, and possibly even videos or animations. This visually appealing presentation can capture customers' attention and create an immersive dining experience.

## 2. Personalised Recommendations and customer managment: a recommendation engine that suggests menu items based on customers' preferences, past orders, dietary requirements, or even their current mood. Customers can also have their own profiles, allowing them to save delivery addresses, view order history, and provide feedback.

## 3. Kitchen Communication: The system needs to facilitate efficient communication between the kitchen and front-of-house staff to ensure accurate and timely order preparation.

## 4. Loyalty Program Integration: Integrate a loyalty program into the ordering system to reward customers for their patronage. Customers can earn points, receive exclusive offers, or enjoy special privileges based on their loyalty status. Th

## 5. Virtual Reality (VR) Dining Experience: I can incorporate virtual reality into the dining experience. Customers can use VR headsets to virtually visit the restaurant's kitchen, observe the food preparation process, or embark on virtual culinary adventures. This immersive technology can add an element of novelty to the dining experience.

## 6. Seamless Mobile Ordering: a mobile app that allows customers to conveniently place orders from their smartphones. This app can feature user-friendly navigation, order tracking, and personalised promotions. The system should securely handle online payments, integrating with payment gateways to process transactions.

## 7. Social Media Integration: Enable customers to share their dining experiences on social media directly from the ordering system. Implement social sharing buttons or hashtags to encourage customers to post food photos, leave reviews, or engage with the restaurant's social media presence. 

Main Considerations and Problems:
## 1. Scalability: The system should be designed to handle a high volume of orders during peak hours without performance issues.

## 2. Integration Challenges: Integrating the ordering system with existing restaurant infrastructure, such as point-of-sale (POS) systems, kitchen display systems, or inventory management tools, may pose technical challenges that need to be addressed.

## 3. Data Security: Implementing good security measures to protect customer information, including payment details, is essential to build trust and maintain customer privacy.

Components or Tools:
## 1.. Mobile App Development Frameworks: Use popular mobile app development frameworks, such as React Native or Flutter, to build a seamless mobile ordering app.

## 2. Recommendation Engine Frameworks: Implement machine learning frameworks like TensorFlow or PyTorch to develop personalized recommendation engines.

## 3. Virtual Reality (VR) Equipment: Consider VR headsets, cameras, and software development tools for creating immersive VR dining experiences.

## 4. Social Media Integration APIs: Utilise social media APIs (e.g., Facebook, Instagram) to enable customers to share their experiences on social platforms directly from the ordering system.

## 5. Secure Payment Gateways: Integrate with secure payment gateways to facilitate online transactions and ensure customer data protection.

## 6. Backend Server: Building a server to handle order processing, manage data, and interact with external services.

## 7. Database: Storing menu information, customer profiles, orders, and other relevant data.

## 8.Payment Gateway Integration: Connecting the system to a payment gateway to securely process online payments.

## 9. Real-time Inventory Tracking: Utilising technologies for real-time monitoring of ingredient availability and inventory management.

## 10. Communication Channels: Implementing notification systems, such as SMS or push notifications, to provide updates to customers and staff.



