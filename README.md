# Discord-MediaWiki-API-Bot
An example of a bot that interacts with MediaWiki API from a Discord client.

This project was designed to be a quick proof-of-concept for a program that receives input via the [Discord](https://discord.com/) application and produces an output depending on what the input was. We leverage the [Discord.py](https://pypi.org/project/discord.py/) library to simplify the reading of inputs from the Discord app, as well as the [mwclient](https://github.com/mwclient/mwclient) library to simplify making API calls. There are simple commands to test that the program is receiving input correctly, as well as a more complex command that gets data from the [Mizuumi Wiki](https://wiki.gbl.gg/w/Main_Page) website using the [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page).

Basic Functions
---
The bot will ignore any messages that do not begin with a `$` character and continuously wait until it sees such a message. When it does, it reads the string following the `$` to determine which command it is and executes the associated action. After this, it returns to waiting for another command.
For example, if one types `$hello` then the bot will respond:

![image](https://github.com/eglopez07/Discord-MediaWiki-API-Bot/assets/9082653/1515150f-e4af-447a-9b35-96773b8581ee)

If one types `$length` the bot will return the character length of the message:

![image](https://github.com/eglopez07/Discord-MediaWiki-API-Bot/assets/9082653/8a3d0232-7089-458a-a795-87f26eed8935)

These simple commands do not have additional arguments; the bot takes in the entire message containing the command as the sole argument.

Cargo Queries
---
The primary function of the bot is to run a query on a database for a MediaWiki site. This is done with the help of MediaWiki's [Cargo extension](https://www.mediawiki.org/wiki/Extension:Cargo). This extension stores data in tables and also makes it available to external users through a specific API action, ["cargoquery"](https://discoursedb.org/w/api.php?action=help&modules=cargoquery).
The specific MediaWiki site we are targeting is predefined in a variable. When the bot reads the command `$fd s` (where `s` is a string of characters) it will run the "cargoquery" API action on the specified site. The various API action parameters are pre-maintained to retrieve a particular value on the table, with only the `s` argument being used to help filter the result.

As an example, if we enter the command `$fd na_5a` then the bot will read that message and turn it into a query equivalent to the following wikitext:

    {{#cargo_query:tables=UNICLR_MoveData|fields=UNICLR_MoveData.moveId, UNICLR_MoveData.damage|where=UNICLR_MoveData.moveId="na_5a"}}

Within the bot program, the API action will return the result in the form of an OrderedDict structure. We can then output the value back to Discord, as shown below:

![image](https://github.com/eglopez07/Discord-MediaWiki-API-Bot/assets/9082653/48bfe697-c4e1-4a40-87fd-5eef71f86372)

To compare, [this link](https://wiki.gbl.gg/w/Special:CargoQuery?title=Special%3ACargoQuery&tables=UNICLR_MoveData%2C+&fields=UNICLR_MoveData.moveId%2C+UNICLR_MoveData.damage%2C+&where=UNICLR_MoveData.moveId%3D%22na_5a%22&join_on=&group_by=&having=&order_by%5B0%5D=&order_by_options%5B0%5D=ASC&limit=&offset=&format=) shows the result of the exact same query as above. As of 07/03/2023, the results should be identical.
![image](https://github.com/eglopez07/Discord-MediaWiki-API-Bot/assets/9082653/7fbe13c7-754f-48ae-8fb1-9b3fe908e0ef)
