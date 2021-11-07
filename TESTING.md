# Testing

- [Encountered Issues](#ecountered-issues)
- [Code Validation](#code-validation)
- [Testing User stories](#testing-user-stories)
- [Testing Functionality](#testing-functionality)
- [Testing Compatibility](#testing-compatibility)
- [Testing Accessibility](#testing-accessibility)
- [Testing Performance](#testing-performance)
- [Further Testing](#further-testing)

## Encountered Issues
---

**Project Bugs And solutions**
---
While working on this project I encountered the following problems which I tried to solve in the following way:
1. ERROR: IntegrityError at/accounts/login/ unique constrant failed:profiles.user_id showed while registering new user and trying to sign in 
![integrity error](wireframes/testing/integrity-error.png)
    SOLVING BY: 
    - Checking for code differences in diffchecker (came out correct) ,
    - Created a new superuser (still left with the same error),
    - Deleted the db.sqlite3 file in workspace, make and run migrations, loaded my fixtures for categories.json and product.json, then created a new superuser (still didn't work)
    - Checked all related files and the issue was forgotten undo uncommited lines in models.py 
        - from
    ![integrity error bug](wireframes/testing/integrity-error-bug.png)
        - to
    ![integrity error solution](wireframes/testing/integrity-error-solved.png)

2. ERROR: while making purchase on the site and receivind an order confirmation on the profile site and success message the confirmation email doesn't appear in the terminal. Instead the error `POST /checkout/wh/HTTP/1.1 500 146184` and TemplateDoesntExist received
![confirmation-email-error](wireframes/testing/confirmation-email-error.png)
    SOLVED BY:
   - Checking for typos and correct place for **confirmation_emails** folder and webhook_handler.py
   - Checking the webhooks are correct, updating in the settings variables, and on the stripe site 
   - The error came from a typo in the `confirmation_email_subject.txt`
![confirmation-email-error-typo](wireframes/testing/confirmation-email-error-typo.png)


3. ERROR: While saving the comment on the "Add Comment" form the Integrity error not hull constraint failed: blog_blogcomment.user_comment_id appear

![integrity-error-comments-blog](wireframes/testing/integrity-error-comments-blog.png)

    SOLVED BY: 
    - changing in models.py BlogComment class comment values `null=True` and `blank=True`
    - wrong spelled name in the views.py `comment_user` => `user_comment`

![integrity-error-comments-blog-solved](wireframes/testing/integrity-error-comments-blog-solved.jpg)
![integrity-error-comments-blog-solved](wireframes/testing/integrity-error-comments-blog-solved1.png)

4. ERROR: While implementing modal a problem with dislayng on the screen

    SOLVED BY:
    - It was a typo in id 
![modal-error](wireframes/testing/modal-error.jpg)

5. BUG: `Delete|Edit` buttons for comments don't hide when user is on his account is able to to see other users buttons

![modal-delete-button-error](wireframes/testing/modal-delete-button-error.jpg)
    SOLVED BY:
    - Changing if statement
![modal-delete-button-error-solved](wireframes/testing/modal-delete-button-error-solved.jpg)
6. ISSUE: While adding missing message field into the models.py in contact form a makemigration non-nullable firld 'message' issue appeared
![makemigrations-contact-message-issue](wireframes/testing/makemigrations-contact-message-issue.png)


![contact-models-message-error](wireframes/testing/contact-models-message-error.jpg)

SOLVED BY: 
- value: null=False changed to null=True
- value: blank-False changed to null=True
7. ISSUE: While testing the contact form message field didn't work as expected (no validation) and also the makemigration message appeared
![make-migration-message](wireframes/testing/make-migration-message.png)
SOLVED BY: 
- in models message atribute value blank=True changed to null=False and null=True stayed the same
- before migrations database with sent emails was deleted
![message-field-issue-solved](wireframes/testing/message-field-issue-solved.jpg)
8. BUG: Input placeholders are not displayed on the Contact page as expected, default labels are enabled.
![message-field-issue-solved](wireframes/testing/forms-placeholders-intendation-bug.png)

SOLVED BY:
- wrong intendation 
![forms-placeholders-intendation-bug](wireframes/testing/forms-placeholders-intendation-bug1.jpg)
9. I encountered a few difficulties when creating a subscription app for the newsletter
    a) BUG : The newsletter-subscription form don't display on the site 
    SOLVED BY: Forgot to add the context to the context processors in settings.py `'contexts.subscription_form',` 
    ![contexts-subscription-form](wireframes/testing/contexts-subscription-form.jpg)
    
    b) ERROR: No Reverse Match at contact/newsletter signup 
     ![no-reverse-match-newsletter-error](wireframes/testing/no-reverse-match-newsletter-error.png)
    SOLVED BY: It was wrong return 'newsletter_form' whis is a value not a URL changed to redirect_url add in footer.html in the form a hidden input field and change view to get the redirect_url from the form and then redirect it to the redirect_url
    ![hidden-input-field](wireframes/testing/hidden-input-field.jpg)
    ![redirect-url](wireframes/testing/redirect-url.jpg)
10. I encountered a few difficulties while deploying project to heroku but main was: 
    a) ISSUE: logo images and hero-images  didn't appear on the on the home page
       SOLVED BY: create a new folder in static folder 'images' and moved the images from media folder to static folder
    b) ISSUE: logo butterfly image didnt wan't to display ftom static/imagef file
       SOLVED BY: It have to be moved back to Media folder and add the MEDIA_URL

    ![butterfly-logo-mobile-top-header](wireframes/testing/butterfly-logo-mobile-top-header.png)

11. While creating review application I  encountered a few errors that two of them:
    a) ERROR: NameError at products/add_review 
    SOLVED BY: Change 'User' to 'UserProfile' for model and in the views 
    form `user = User.objects.get(user=request.user)` to ` user = get_object_or_404(UserProfile, user=request.user)`
    ![review-user profile-error](wireframes/testing/review-user profile-error.jpg)

    b) ISSUE: Comments don't display on the product_detail site product. Product review object is returning from the view but don't display data on the site.

    ![review-if-statement-issue](wireframes/testing/review-if-statement-issue.jpg)

      SOLVED BY: create the if statement review that checks if there are any reviews and then loop through them. As the product review is already retrived from DB in the view we don't need to create any associacion with produce in the frontend like it was done previously.

    ![review-if-statement-issue-sollution](wireframes/testing/review-if-statement-issue-sollution.jpg)
12. ISSUE: Static Files didn't uploaded on Heroku live website after changes on gitpod
    SOLVED BY: 
    - Changed STATICFILES_DIRS and add STATIC_ROOT to settings.py
    - Added variables to GitPod variables on settings from heroku DATABASE_URL and DEVELOPMENT set to False, make sure DEVELOPMENT doesn't exist on the Heroku config variables.
    then make sure to close and reopen worksace again for project 
    - run the command `python3 manage.py collectstatic` (staticfiles added to static folder)

    BEFORE:
    ![old-static-url](wireframes/testing/old-static-url.png)
   
    AFTER:
    ![updated-static-url](wireframes/testing/updated-static-url.png)

13. ISSUE: The  Review `Edit | Delete` buttons are visible only for a superuser, not for the owner of the review, and they are not able to edit or remove their reviews. 

    SOLVED BY: Initialy the if statement was checking two variables that are different of types. After changes `Edit | Delete ` links will be visible to the user if they are logged in and they are own the review. 
        - Make a new variavle `review_user` in the edit_review view 
        - Add to the product_detail a `review_user = None` and if statement
        - Modify if statement in a product_detail.html 
    
    BEFORE CHANGES:
    ![review-if-stetement-product-detail-issue](wireframes/testing/review-if-stetement-product-detail-issue.png)
   
    AFTER CHANGES:
    ![review-if-statement-edit-review](wireframes/testing/review-if-statement-edit-review.jpg)
    ![review-if-statement-product-detail](wireframes/testing/review-if-statement-product-detail.jpg)
    ![review-if-statement-product-detail-html](wireframes/testing/review-if-statement-product-detail-html.jpg)

14. ISSUE: The problem with displaying and counting the average rating for each product

    SOLVED BY:

    - Add signals in the Product app, which will fire whenewer the `Review` is created  for that product and register signal in apps.py
    - modify the calculate_rating method
    
    BEFORE CHANGES:
    ![calculate-ratings-before](wireframes/testing/calculate-rating-before.jpg)
    
    AFTER CHANGES:
    - remove all() as the aggregation implies all items already
    - remove the return as the method only calculates the average rating and sets it and don't return anything

    ![calculate-ratings-after](wireframes/testing/calculate-ratings-after.png)

15. ERROR: While testing the sorting by: `Rating(low to high) Rating(hight to low) `future the error field appeared

    ![sort-by-rating-error](wireframes/testing/sort-by-rating-error.png)

    SOLVED BY:
    - As the `rating` sortkey will only sort the non-null vs null items the new variable `subkey` is created  to sort products on the actual avg_rating.
    - The desc will invert the sortkey so it was needed to put sortkey and the subkey into the id direction statement

    ![main-nav-sort-by-rating](wireframes/testing/main-nav-sort-by-rating.png)
    ![products-sort-rating-by](wireframes/testing/products-sort-rating-by.png)
    ![views-sort-by-rating-solution](wireframes/testing/views-sort-by-rating-solution.jpg)

## Code Validation
---

## Testing User stories
---

## Testing Functionality



### Checking for broken links
---


### Responsive Design
---


 **Encountered problems while testing the site on different devices**
 



## Testing Compatibility
---

---
## Testing Performance
---


## Testing Accessibility
----


- **Accessibility for mobile devices on LightHouse**


## Further Testing


### Overflow
