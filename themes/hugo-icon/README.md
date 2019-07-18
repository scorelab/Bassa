# Icon Theme

This theme is a Hugo port of the icon theme by [https://freehtml5.co/](https://freehtml5.co/icon-free-website-template-using-bootstrap/). It is a single-page, responsive theme, with sections for describing your business mission, services, a gallery, your team and a contact form.

![](images/screenshot.png)

## Installation

Follow the themes guide on the [Hugo website](https://gohugo.io/themes/installing-and-using-themes/). Briefly, within your Hugo folder:

```sh
$ cd themes
$ git clone https://github.com/SteveLane/hugo-icon.git
```

## Getting started

Copy `exampleSite/config.toml` into the root of your website folder, and edit it to your hearts content!

Add `theme = "hugo-icon"` to this config, or when serving, use `hugo server -t hugo-icon`.

## Adding additional pages

If you'd like to add additional pages, say for a blog, place your content in `/content/blog/` (with an `_index.md` and additional markdown files for each entry).

To link to it from the main menu, add the following line to `layouts/partials/nav.html`:

```html
<a href="/blog" onclick="location.href='/blog';">Blog</a>
```

## Credits

Credit for this theme goes fully to [https://freehtml5.co/](https://freehtml5.co/), which is licensed under a [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) license. If you use this Hugo port, please consider the terms of that license and make proper attribution to [https://freehtml5.co/](https://freehtml5.co/).

## Changelog

A changelog for the initial port by @SteveLane is [here](changelog.md); if you fork this theme and make changes, please list them.
