Title: My work
Date: 2024-10-05
Category: Portfolio

- [Looker](#looker)
- [Power BI](#power-bi)
- [Python](#python)
- [R packages](#r-packages)
- [Shiny](#shiny) (Python/R dashboarding app)
- [Websites](#websites)

Please note this is by no means a comprehensive overview of my work. However, a I cannot publicly share much of what I have done in my employment, so a lot of this content is what I've managed to cobble together in my spare time.

## Looker

I was the lead developer on Digital Science's [Dimensions Research Integrity](https://www.dimensions.ai/products/all-products/dimensions-research-integrity/) Looker app. I also helped to maintain and improve their core Looker data model.

__Note__: You won't be able to view the actual app without signing up for it.

## Power BI

Here is a relatively simple dashboard showing some New Zealand climate data.This is based on a star-schema model of data taken from CliFlo (now replaced by [DataHub](https://data.niwa.co.nz/)).

<iframe title="nz_climate_dashboard" width="100%" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiNjhmNDRmMzYtNWQ4Mi00ZTIxLWFlNzAtNjRlOTlhN2RhNmMwIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>

I have also produced dozens of (more complex) Power BI reports for the University of Exeter, but these data are confidential.

## Python

A high proportion of my Python work is behind orgnisational barriers unfortunately.

This website is not, though! I built it using the `pelican` package; you can view the [source code on GitHub](https://github.com/shanej90/shanej90.github.io).

I did produce a Dash dashboard for modelling 'quality-related' research funding between the release of the [2021 Research Excellence Framework](https://2021.ref.ac.uk/) and the announcement of the funding. Unfortunately it was hosted on Heroku's free tier which has since been withdrawn, so I need to find a new home for it. You can still see the [source code](https://github.com/shanej90/qr_modelling).

Whilst at Digital Science I did do some work on the [Dimensions API Labs](https://api-lab.dimensions.ai/), a series of Jupyter Notebooks designed to help users interact with the Dimensions API via the `dimcli` Python package. __My contributions are small__, but some of my stuff is up there. The [source code is on GitHub](https://github.com/digital-science/dimensions-api-lab).


## R packages

Although most of my R packages are in a private work repo, there are some public ones I can share:

- [gtR](https://github.com/shanej90/gtR): Wrapper for the UK Research and Innovation [Gateway to Research](https://gtr.ukri.org/) API. You can also see the [documentation](https://shanej90.github.io/gtR/).
- [nodemaker](https://github.com/shanej90/nodemaker): Tool for preparing data for use in network diagrams. You can also see the [documentation](https://shanej90.github.io/nodemaker/).
- [ror4r](https://github.com/shanej90/ror4r): Wrapper for the [Research Organization Registry](https://ror.org/) API. You can also see the [documentation](https://shanej90.github.io/ror4r/).
- [ukcpR](https://github.com/shanej90/ukcpR): Wrapper for the UK Met Office [UK Climate Projections](https://ukclimateprojections-ui.metoffice.gov.uk/ui/home) API. You can also see the [documentaton](https://shanej90.github.io/ukcpR/).

These are all 'development' packages; none are on CRAN.

## Shiny

Continuing on the climate theme, here is a dashboard of climate averages for select locations around the globe. This data was obtained from Wikipedia and loaded to a `sqlite` database. The process for doing this is available on [GitHub](https://github.com/shanej90/wiki_climate_data). (PS. The way I am reading in the data and handling it on user input is not best practice, but for a small dataset it works).

<iframe height="400" width="100%" frameborder="no" src="https://shanej90.shinyapps.io/wikipedia_climate_data/"> </iframe>

I also have a (very basic) investment returns calculator. The code is also on [GitHub](https://github.com/shanej90/investment_returns).

<iframe height="400" width="100%" frameborder="no" src="https://shanej90.shinyapps.io/investment_return_shiny/"> </iframe>

## Websites

As mentioned in the [Python](#python) section, I made this website using Python, via the `pelican` package. View the [source code](https://github.com/shanej90/shanej90.github.io) if interested.