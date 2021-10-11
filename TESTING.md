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
    - Checking for cod differences in diffchecker (came out correct) ,
    - Created a new superuser (still left with the same error),
    - Deleted the db.sqlite3 file in workspace, make and run migrations, loaded my fixtures for categories.json and product.json, then created a new superuser (still didn't work)
    - Checked all related files and the issue was forgotten undo uncommited lines in models.py 
        - from
    ![integrity error bug](wireframes/testing/integrity-error-bug.png)
        - to
    ![integrity error solution](wireframes/testing/integrity-error-solved.png)


    
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
