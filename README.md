# ScotBot
Requested by Scotti to poll reactions

Simmple and for now I guess.

## Setup
0. run `pip install -r requirements.txt`
1. Create a `.env` file in the same folder as scotbot.py
2. Add `SCOT_TOKEN=REPLACE_WITH_YOUR_TOKEN` and save
3. Run scotbot.py when ready

How this works:
1. React with 🏁 (:checkered_flag:) on a message to receive a DM from ScotBot with a list of reactions and the users who reacted with that reaction.
Note: This only works for messages that have been sent since the bot has been running. If the message and reactions were sent before the bot started up, it has no access to getting the reactions.

That's it, you're done. :)

#### Notes
All this does is look at reactions at the moment. No need to give it admin privileges. Read message history should be fine.
