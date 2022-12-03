### Side projects are a way for you to experiment with new ideas in software engineering and challenge your ability to create from scratch.

They are also an opportunity for you to improve your documentation skills by writing up a high level overview and how you made the project. If you're interested in working on a side project, first talk to your mentor about your interests (ex. "Frontend engineering is my favorite!"). Then, work with the mentor to 

1) Identify an area of CS you're interested in working on (ex API designs).

2) Do some basic research with your mentor. If there is a roadmap that supports your area of interest (ex the Backend Roadmap is related to API designs), then review some of that material and pick something you find intriguing.

3) After picking an area of interest (we will use "RPC APIs" as our example) find some relevant sources to support building your project. You may want to find popular, industry standard packages that would support the project (ex. Google's RPC framework gRPC), a quickstart tutorial on the topic (ex. "Your First gRPC API!"), some lectures (ex. a video called "Comparing REST, RPC, and GraphQL" on Youtube), and any external API's (ex. https://randomuser.me/ ) you might need to get data for your project.

4) Review, compile, and formalize these sources then bring them to your mentor with an idea of what you might want to build. You can make a copy of this [template](https://docs.google.com/document/d/1kP8c33G6GC1A0hgnL7aDTuVNtFnV7XEkyZ0zabn1nUg/edit?usp=sharing) to help you formalize the project plan. Remember, these side projects are your own, so feel free to put your own twist on them. For example, if you like chess try to make your RPC API communicate between two different services to conduct a chess match.

5) Once your plan is peer-reviewed by a mentor, put up a short summary in our communications (currently the #side-projects channel in Slack) to see what the community thinks. Maybe someone is an expert or has experience in this topic - this is invaluable information to have when going into an unfamiliar domain.

6) Go ahead and get started on your project! Make sure you create a repository for it on your Github account so you can push to it, have others use this to provide support whenever you need it (screen sharing code and running it can be a pain!), have this project contribute to your resume, and be a part of the open-source community (make sure its a public repository).

7) Once you complete and peer review the project, you will want to add your side project's github repository as a submodule to our own repository. We will classify side projects in the following categories - fullstack, frontend, backend, data science, and other. If your project combines elements of two different categories, try to place it in the directory you think it has more focus on.

To place your repo in our CSX repo as a submodule, cd into the "csx" folder and run the following command filled in with your information.

`git submodule add [side project github repo url] [destination folder]`

- The side project github repo would be something like "github.com/your_username/your_side_project".
- The destination folder would be something like `./side_projects/server`, if your project was server-focused.
