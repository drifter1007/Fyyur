from app import db, Venue, Artist


def stest():
    file1 = open("/vagrant/Fyyur/ntr.txt", "wt")
    file1.write(str(' '))
    file1.close()
    areas1 = db.session.query(Venue).distinct(
        Venue.state, Venue.city).all()
    # areas = Venue.query.filter_by(
    #        state=Venue.state).filter_by(city=Venue.city).all()
    data = []
    for area in areas1:
        areas2 = Venue.query.filter_by(
            state=area.state).filter_by(city=area.city).all()
        venue_data = []
        for venue in areas2:
            venue_data.append({
                "id": venue.id,
                "name": venue.name
            })
        data.append({
            "city": area.city,
            "state": area.state,
            "venues": venue_data
        })
    file1 = open("/vagrant/Fyyur/ntr.txt", "at")
    file1.write("\n **Final Venue_data** \n")
    file1.write(str(venue_data))
    file1.close()
    file1 = open("/vagrant/Fyyur/ntr.txt", "at")
    file1.write(' \n **Data** \n')
    file1.write(str(data))
    file1.close()
    # print(data)


stest()
