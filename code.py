fuck ai

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
  [] decomposition page(like in notion or this file: (projects, tabs, checkboxs, if done = gray)
    [] projects(steal from old project)
      # [x] create add project button
      # [x] create project page(only name input)
        # [x] api(projects model(id, user_id, name), controller)
        # [x] save button, back button, request to api
        # [x] add frontend validation(not empty)
      # [x] show list of projects
        # [x] indent from footer
        # [x] add link(id)
      [] project page
        # [x] delete project button
        [] tasks(copy from notion)
          # [x] task(id, project_id, is_complete, tabs, content) -mcr
          [] textarea
            # [x] off borders, make background equal to body, off arrow
            [] every enter = new checkbox [x] from old project, which i can't change, only click
            [] up and down key = up and down text
            [] backspace on checkbox = delete checkbox if tabs = 0 or tabs - 1
            [] checkbox on hover - gray + may be some animation(old project with bootstrap)
            [] implement tabs(space on phone, tab or space on pc)
            [] if checkbox checked - make text gray
          [] implement save button(delete all previous and save all new tasks)
          [] implement delete button
  [] footer(projects, timer) component
      [] highlight current page
  [] timer page(default timer(pause, reset, start, set time))
  [] if api return 401 - delete token
  [] readme installation guide
  [] api docs(scramble/?)
  [] ?collab
  [] get feedback(tg chat)

[] anime site

[] сайтик или приложение(или 2 в одном) как блокнотик короч. ну вот в жизни. чисто записная книжка, как в golden boy со страничками и листанием

[] cbt app with statistics(diet, consistent sleep, exercises, meditations)
