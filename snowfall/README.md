
# Snowfall

Roll a foreground image over a background.

Used to create the Shinobuugakoa gif:

![Cherry blossom falling past a samurai](shinobugaoka.gif)

From the original

[Shinobugaoka no tsuki-Gyokuensai from Europeana](https://www.europeana.eu/portal/en/record/9200424/oai_digitool_bibnat_ro_246569.html)

![Still image from Europeana](full_eg.png)

I used GIMP to manually turn this into the three files

![Samurai without blossom](bg_eg.png)
![Blossom only](fg_eg.png)
![Mask border and labels](mask_eg.png)

`python snowfall.py bg_eg.png fg_eg.png, mask_eg.png`
