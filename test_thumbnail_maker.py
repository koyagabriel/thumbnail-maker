from thumbnail_maker import ThumbnailMakerService

IMG_URLS = \
    ['http://static01.nyt.com/images/2015/10/25/t-magazine/25tmag-11well_rihanna-t_CA0/25tmag-11well_rihanna-t_CA0-facebookJumbo.jpg',
     'http://cdn.vox-cdn.com/thumbor/pNDBuwzwchiSjOWuH81YiS0ydGo=/0x0:4510x2830/1200x800/filters:focal(2062x775:2782x1495)/cdn.vox-cdn.com/uploads/chorus_image/image/59041229/849725174.jpg.0.jpg',
     'http://fashionista.com/.image/t_share/MTUyMDQ2NjY2ODY4ODYwODEw/fenty-lipstick.jpg',
     'http://www.media4.hw-static.com/wp-content/uploads/beyonce-mod-fashion-gallery-btr_56844836-1768x1200.jpeg',
     'http://1.bp.blogspot.com/-h9-6bt81s7U/TmSqBI8l6MI/AAAAAAAAAsg/JFNhhnpe4Ak/s1600/Beyonce+Knowles+Photo+Gallery.jpg' 
    ]
    
def test_thumbnail_maker():
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
