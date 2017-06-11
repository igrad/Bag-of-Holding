# Bag-of-Holding
Bag of Holding is a cross-platform mobile app for maintaining inventory in RPG tabletop games, such as Dungeons and Dragon. This project is named after the "Bag of Holding" item from Dungeons & Dragons, and is intended as a small play on the well-known item. The app is intended for both iOS and Android platforms, and may support Windows mobile platforms down the road if Kivy begins to support it.

The targeted release for this project is early 2018, though that is certainly subject to change this early in development.

This is intended to be released as a free app, with options for donations. There will be no ads for revenue; this is simply a small contribution to the gaming community, not my source of income.

## Development preview

Main Menu | Selected Item
--------- | -------------
![Main Menu](https://puu.sh/whnRT/f5757abe40.jpg) | ![Selected Item](https://puu.sh/whnMd/421cd31226.jpg)

## Tasks
- [x] Design of core menus
- [ ] Design of ***Bags*** and ***Settings*** menus
- [ ] Implementation of ***Bags*** and ***Settings*** buttons
- [x] Implementation of ***Tabs*** buttons
- [x] Create new item from ***New*** button in ***Tabs***
- [ ] Reorder items using ***Sort*** button in ***Tabs***
- [x] Change view type using ***View*** button in ***Tabs***
- [x] Implementation of ***Search Bar***
- [x] Search after 0.5s delay using auto-filtering
- [x] Search using keywords in query, such as qty, weight, val & some synonyms
- [x] Implementation of ***ContPane***
- [x] ***ItemView*** selection methods (a.k.a. ***Select***)
- [x] Edit item data in ***Select*** window
- [x] Edit item Icon in ***Select*** window
- [ ] Design of ***Options*** sub-menu in ***Select*** window
- [ ] Options to delete item, move item to another bag, share item, create printable version of item card


### Technical
As mentioned above, this is built using <a href="https://www.python.org/downloads/release/python-344/">Python 3.4.4</a> and <a href="https://kivy.org/docs/gettingstarted/intro.html">Kivy 1.10.0</a>. This project is being released for public use under the GPL 3.0 license, in keeping with Kivy and Python's respective licensing. Please see the LICENSE file for further licensing information.

### Credits
* **Ian Gradert** - Design, all coding, all artwork except for item icons
* **www.game-icons.net** - All item icons
