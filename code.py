mobile first
fuck good code, write code that works
optimize if u NEED this after product done

[] code helper(vue spa + laravel api(token auth))
  # [x] setup(cd backend && ./vendor/bin/sail up -d && cd ../frontend && npm run dev)
  # [x] git repo
  # [x] vue router course https://vueschool.io/courses/vue-router-4-for-everyone - skipped
  # [x] token auth (Sanctum)
    # [x] crete frontend register and login page
    # [x] create login and register api
      # [x] register api: get name, email, password + return token + create user in db
      # [x] login: get email, password + return token
    # [x] connect frontend to api
      # [x] frontend validation
        # [x] don't allow empty from frontend(red input and red text under input), add password confirm = password validation
        # [x] bug: why laravel api send me html instead of json? - 'Accept': 'application/json'
        # [x] bug: if any error in console: has been blocked by CORS policy: No 'Access-Control-Allow-Origin'... - 'Accept': 'application/json'
        # [x] show errors from backend(red text under input)
      # [x] save token in localstorage
      # [x] implement redirect
      # [x] frontend redirect if user don't have token in localstorage
      # [x] redirect from register and login if user authorized
  # [x] decomposition page(like in notion or this file: (projects, tabs, checkboxs, if done = gray)
    # [x] projects(steal from old project)
      # [x] create add project button
      # [x] create project page(only name input)
        # [x] api(projects model(id, user_id, name), controller)
        # [x] save button, back button, request to api
        # [x] add frontend validation(not empty)
      # [x] show list of projects
        # [x] indent from footer
        # [x] add link(id)
      # [x] project page
        # [x] delete project button
        # [x] tasks(copy from notion)
          # [x] task(id, project_id, is_complete, tabs, content) -mcr
          # [x] textarea
            # [x] off borders, make background equal to body, off arrow
            # [x] checkbox from old project
            # [x] on click enter - append new task to data() with id+1 and text '' + change focus to new input
            # [x] now i want to add new task and set focus after the current task, not at the end
            # [x] then i click ↑ ↓ change focus to index-1 or index+1
            # [x] implement tabs(space on phone, tab or space on pc in input start)
              # [x] if cursor on position == 0 and i press tab or space: +1 to tab in array(1 tab = +35px margin left)
            # [x] backspace on checkbox = delete checkbox if tabs = 0 or tabs - 1
            # [x] if checkbox checked - make text and checkbox gray
            // # [] checkbox on hover - gray + may be some animation(old project with bootstrap)
            # [x] add hints(tab, space, delete)
            // # [] bug: arrows can only navigate from elem to elem, currently they cannot navigate through text
          # [x] implement save button(delete all previous and save all new tasks)
            # [x] send array on frontend
            # [x] get array on backend
            # [x] delete all tasks from project
            # [x] save all new tasks to project 
          # [x] implemeте receiving tasks from the api after going to the tasks page
            # [x] return tasks only for this projects?
            # [x] if return empty array - create {checkbox: false, text: '', tabs: 0}
          # [x] implement delete button
            # [x] api for delete
            # [x] frontend implementation
                # [x] request
                # [x] confirmation popup
          # [x] popup if i quit and don't save edited tasks
            # [x] save tasks when created() on oldTasks
            # [x] changesCheck method: (if on back button oldTasks != tasks): popup(backToMain) with message: Changes are not saved, want to quit?
          # [x] bug: after task with 3 tabs i can't implement any tabs, although it was expected that I would be able to create a new task with 2-4 tabs
# [x] if api return 401 - delete token - in main.js
# [x] bug: after delete user i still can navigate from app with old token - solved after if 401 await originalFetch(url, options) - delete; in main js
  # [x] footer(projects, timer) component
      # [x] highlight current page
  [] timer page(default timer(pause, reset, start, set time))
    # [x] footer
    # [x] timer frontend https://excalidraw.com/#json=ifV5YyeHO12rr3IWUnLa3,1sD7j2IEcQ_iZ7M6wX9yiQ
      # [x] create timer
        # [x] input buttons
        # [x] display digits on timer
          # [x] from [1, 2, 3, 4] display 00h, 12m, 34s
          # [x] model Timer(id, user_id, start_time, duration)
          # [x] save to db(request, controller)
      # [x] get timers from api
      # [x] if timer >=1: displayTimer component, else: createTimer component
      [] displayTimer frontend
    [] bug: fix 0 input
    [] bug: i can see startTimer before I get a response from the API
  [] white download indicator on top
  [] pc version frontend optimization
    [] hover buttons style on pc
  [] refactor(computed, improve csrf, token(now don't have foreign key to user_id. should?), ?token in cookie ...)
    [] cors config
  [] readme installation guide
  [] api docs(scramble/?)
  [] create release branch
  [] ?collab
  [] get feedback(tg chat)

[] anime site

[] сайтик или приложение(или 2 в одном) как блокнотик короч. ну вот в жизни. чисто записная книжка, как в golden boy со страничками и листанием

[] cbt app with statistics(diet, consistent sleep, exercises, meditations)
