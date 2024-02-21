# Scratch-Search-Engine
Lets you run a search engine in Scratch!

### Instructions
- Go to https://serpapi.com/ and get a free API key
- Create a `.env` file in the same folder as `main.exe`
- Add `API_KEY=YourKeyHere`
- Go to Scratch, press ctrl + shift + i, click network, press ctrl + r to refresh the page, search session, and on the right side bar in the headers tab, scroll and look for cookie, then grab everything in the quotes after `scratchsession=`
- Go back to your .env and add `SCRATCH_TOKEN=` and then your token
- Enter your Scratch username, ex `SCRATCH_USERNAME=Stoutscientist`
- Add your Scratch project, ex `SCRATCH_PROJECT=967768776`
- Run the EXE!
