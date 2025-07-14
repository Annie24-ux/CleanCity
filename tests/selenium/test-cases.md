# CleanCity – Test Cases & Checklists

---

## 1. Functional Test Cases

| Test Case ID | Scenario                                 | Test Steps                                                                                       | Expected Result                                      | Actual Result | Bug Ref |
|--------------|------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------|--------------|---------|
| TC-01        | User Registration                        | 1. Go to Register page<br>2. Fill valid details<br>3. Submit                                     | User account created, redirected to Home             |              |         |
| TC-02        | User Login                               | 1. Go to Login page<br>2. Enter valid credentials<br>3. Submit                                   | User logged in, dashboard visible                    |              |         |
| TC-03        | Schedule Waste Pickup                    | 1. Login<br>2. Go to Schedule Pickup<br>3. Fill form<br>4. Submit                               | Pickup scheduled, confirmation shown                 |              |         |
| TC-04        | Dashboard Access (Authenticated)         | 1. Login as any user<br>2. Navigate to `/dashboard`                                             | Dashboard loads with user data                       |              |         |
| TC-05        | Dashboard Access (Unauthenticated)       | 1. Ensure logged out<br>2. Navigate to `/dashboard`                                             | Redirected to Login component                        |              |         |
| TC-06        | Admin Panel Access (Admin only)          | 1. Login as admin<br>2. Go to `/admin`                                                          | Admin panel loads                                    |              |         |
| TC-07        | Admin Panel Access (Non-admin)           | 1. Login as regular user<br>2. Go to `/admin`                                                   | Redirected to Login component                        |              |         |
| TC-08        | Blog Post Creation (Admin)               | 1. Login as admin<br>2. Go to Blog Admin<br>3. Create new post                                  | Post appears in blog list                            |              |         |
| TC-09        | Blog Home Loads                          | 1. Navigate to `/blog`                                                                          | BlogHome component is displayed                      |              |         |
| TC-10        | Blog Article Loads                       | 1. Navigate to `/blog/1` (or any valid id)                                                      | BlogArticle component is displayed                   |              |         |
| TC-11        | Blog Admin (Admin only)                  | 1. Login as admin<br>2. Navigate to `/blog/admin`                                               | BlogAdmin component loads                            |              |         |
| TC-12        | Blog Admin (Non-admin)                   | 1. Login as regular user<br>2. Navigate to `/blog/admin`                                        | Redirected to Login component                        |              |         |
| TC-13        | Community Feed Post                      | 1. Login<br>2. Go to Community<br>3. Create post                                                | Post appears in feed                                 |              |         |
| TC-14        | Community Feed Loads                     | 1. Navigate to `/community`                                                                     | CommunityFeed component is displayed                 |              |         |
| TC-15        | Awareness Page Loads                     | 1. Navigate to `/awareness`                                                                     | Awareness component is displayed                     |              |         |
| TC-16        | Feedback Submission (Authenticated)      | 1. Login<br>2. Go to Feedback<br>3. Submit feedback                                             | Confirmation message shown                           |              |         |
| TC-17        | Feedback (Unauthenticated)               | 1. Ensure logged out<br>2. Navigate to `/feedback`                                              | Redirected to Login component                        |              |         |
| TC-18        | Profile (Authenticated)                  | 1. Login as any user<br>2. Navigate to `/profile`                                               | Profile component loads                              |              |         |
| TC-19        | Profile (Unauthenticated)                | 1. Ensure logged out<br>2. Navigate to `/profile`                                               | Redirected to Login component                        |              |         |
| TC-20        | Login/Logout Flow                        | 1. Navigate to `/login`<br>2. Login<br>3. Click Logout button                                   | User is logged out, redirected to `/`                |              |         |
| TC-21        | Register Flow                            | 1. Navigate to `/register`<br>2. Register<br>3. Redirect to `/login`                            | User can login after registration                    |              |         |
| TC-22        | Navbar Links (Unauthenticated)           | 1. Ensure logged out<br>2. Observe navbar                                                       | Only Home, Blog, Community, Awareness, Login, Register visible |         |
| TC-23        | Navbar Links (Authenticated)             | 1. Login as regular user<br>2. Observe navbar                                                   | Profile, NotificationBell, Logout visible            |              |         |
| TC-24        | Navbar Links (Admin)                     | 1. Login as admin<br>2. Observe navbar                                                          | Admin link visible                                   |              |         |
| TC-25        | Responsive Design (Mobile)               | 1. Open app on mobile<br>2. Navigate all pages                                                  | Layout adapts, no overflow or cut-off                |              |         |

---

## 2. UI/UX Checklist

- [ ] All navigation links are visible and accessible
- [ ] Buttons and forms have clear labels
- [ ] Error messages are shown for invalid input
- [ ] Consistent color scheme and branding
- [ ] No overlapping or cut-off elements on any device

---

## 3. Accessibility Checklist

- [ ] All images have alt text
- [ ] Sufficient color contrast for text/background
- [ ] All interactive elements are keyboard accessible
- [ ] Screen reader announces page titles and headings
- [ ] Forms have associated labels

---

## 4. Cross-Browser Checklist

- [ ] Chrome: All features work as expected
- [ ] Firefox: All features work as expected
- [ ] Edge: All features work as expected
- [ ] Safari: All features work as expected

---

*Update actual results and bug references as you execute tests and discover issues. Link any bugs to the

Title: User Registration (TC-01)

Steps to Reproduce:

Go to Register page

Fill valid details

Submit

Expected: User account created, redirected to HomeActual: [Pending]Severity: High

Title: User Login (TC-02)

Steps to Reproduce:

Go to Login page

Enter valid credentials

Submit

Expected: User logged in, dashboard visibleActual: [Pending]Severity: High

Title: Schedule Waste Pickup (TC-03)

Steps to Reproduce:

Login

Go to Schedule Pickup

Fill form

Submit

Expected: Pickup scheduled, confirmation shownActual: [Pending]Severity: High

Title: Dashboard Access (Authenticated) (TC-04)

Steps to Reproduce:

Login as any user

Navigate to /dashboard

Expected: Dashboard loads with user dataActual: [Pending]Severity: High

Title: Dashboard Access (Unauthenticated) (TC-05)

Steps to Reproduce:

Ensure logged out

Navigate to /dashboard

Expected: Redirected to Login componentActual: [Pending]Severity: Medium

Title: Admin Panel Access (Admin only) (TC-06)

Steps to Reproduce:

Login as admin

Go to /admin

Expected: Admin panel loadsActual: [Pending]Severity: High

Title: Admin Panel Access (Non-admin) (TC-07)

Steps to Reproduce:

Login as regular user

Go to /admin

Expected: Redirected to Login componentActual: [Pending]Severity: High

Title: Blog Post Creation (Admin) (TC-08)

Steps to Reproduce:

Login as admin

Go to Blog Admin

Create new post

Expected: Post appears in blog listActual: [Pending]Severity: High

Title: Blog Home Loads (TC-09)

Steps to Reproduce:

Navigate to /blog

Expected: BlogHome component is displayedActual: [Pending]Severity: Low

Title: Blog Article Loads (TC-10)

Steps to Reproduce:

Navigate to /blog/1 (or any valid id)

Expected: BlogArticle component is displayedActual: [Pending]Severity: Low

Title: Blog Admin (Admin only) (TC-11)

Steps to Reproduce:

Login as admin

Navigate to /blog/admin

Expected: BlogAdmin component loadsActual: [Pending]Severity: High

Title: Blog Admin (Non-admin) (TC-12)

Steps to Reproduce:

Login as regular user

Navigate to /blog/admin

Expected: Redirected to Login componentActual: [Pending]Severity: High

Title: Community Feed Post (TC-13)

Steps to Reproduce:

Login

Go to Community

Create post

Expected: Post appears in feedActual: [Pending]Severity: Medium

Title: Community Feed Loads (TC-14)

Steps to Reproduce:

Navigate to /community

Expected: CommunityFeed component is displayedActual: [Pending]Severity: Low

Title: Awareness Page Loads (TC-15)

Steps to Reproduce:

Navigate to /awareness

Expected: Awareness component is displayedActual: [Pending]Severity: Low

Title: Feedback Submission (Authenticated) (TC-16)

Steps to Reproduce:

Login

Go to Feedback

Submit feedback

Expected: Confirmation message shownActual: [Pending]Severity: Medium

Title: Feedback (Unauthenticated) (TC-17)

Steps to Reproduce:

Ensure logged out

Navigate to /feedback

Expected: Redirected to Login componentActual: [Pending]Severity: Medium

Title: Profile (Authenticated) (TC-18)

Steps to Reproduce:

Login as any user

Navigate to /profile

Expected: Profile component loadsActual: [Pending]Severity: Medium

Title: Profile (Unauthenticated) (TC-19)

Steps to Reproduce:

Ensure logged out

Navigate to /profile

Expected: Redirected to Login componentActual: [Pending]Severity: Medium

Title: Login/Logout Flow (TC-20)

Steps to Reproduce:

Navigate to /login

Login

Click Logout button

Expected: User is logged out, redirected to /Actual: [Pending]Severity: High

Title: Register Flow (TC-21)

Steps to Reproduce:

Navigate to /register

Register

Redirect to /login

Expected: User can login after registrationActual: [Pending]Severity: High

Title: Navbar Links (Unauthenticated) (TC-22)

Steps to Reproduce:

Ensure logged out

Observe navbar

Expected: Only Home, Blog, Community, Awareness, Login, Register visibleActual: [Pending]Severity: Medium

Title: Navbar Links (Authenticated) (TC-23)

Steps to Reproduce:

Login as regular user

Observe navbar

Expected: Profile, NotificationBell, Logout visibleActual: [Pending]Severity: Medium

Title: Navbar Links (Admin) (TC-24)

Steps to Reproduce:

Login as admin

Observe navbar

Expected: Admin link visibleActual: [Pending]Severity: Medium

Title: Responsive Design (Mobile) (TC-25)

Steps to Reproduce:

Open app on mobile

Navigate all pages

Expected: Layout adapts, no overflow or cut-offActual: [Pending]Severity: Medium


