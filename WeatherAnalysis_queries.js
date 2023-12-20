printjson("****************************************************************");
printjson("1) Get call letters, quality control process, and air temperature from coldest 5 documents (by air temperature) with call letters PLAT and type of FM-13 (logical and, sort)");
printjson(db.data.find({$and: [{type: 'FM-13'}, {callLetters: 'PLAT'}]}, {type: 1, callLetters: 1, qualityControlProcess: 1, airTemperature: 1}).sort({'airTemperature.value': 1}).limit(5))

printjson("****************************************************************");
printjson("2) Get ceiling height and sea surface temperature from coldest 3 sea surface temps with ceiling height <= 22000 or sea surface temperature >= 10 (logical or, range, embedded filter - 1 and 2 layers deep, sort)");
printjson(db.data.find({$or: [{"skyCondition.ceilingHeight.value": {$lte: 22000}}, {"seaSurfaceTemperature.value": {$gte: 10}}]}, {"skyCondition.ceilingHeight.value": 1, "seaSurfaceTemperature.value": 1}).sort({"seaSurfaceTemperature.value": 1}).limit(3))

printjson("****************************************************************");
printjson("3) Get dew point and pressure for data with dew point <= 5 and pressure = 1005, sort by dew point ascending (logical and, range, sort)")
printjson(db.data.find({$and: [{"dewPoint.value": {$lte: 5}}, {"pressure.value": 1005}]}, {"_id": 0, "dewPoint.value": 1, "pressure.value": 1}).sort({"dewPoint.value": 1}))

printjson("****************************************************************");
printjson("4) Get wind speed rate and wind direction angle for slowest 3 (by wind speed rate) data points out of the data points with wind speed rate >= 25 or wind direction angle = 260 (logical or, range, embedded - 2 layers, sort)")
printjson(db.data.find({$or: [{"wind.speed.rate": {$gte: 25}}, {"wind.direction.angle": 260}]}, {"_id": 0, "wind.speed.rate": 1, "wind.direction.angle": 1}).sort({"wind.speed.rate": 1}).limit(3))

printjson("****************************************************************");
printjson("5) Get discrepancy of estimated observation precipitation for data points where discrepancy of estimated observation precipitation is '5' (embedded - 1 layer)");
printjson(db.data.find({"precipitationEstimatedObservation.discrepancy": "5"}, {"_id": 0, "precipitationEstimatedObservation.discrepancy": 1}))

printjson("****************************************************************");
printjson("6) Get wind type and wind speed rate for 5 slowest winds (embedded - 1 and 2 layers, sort)");
printjson(db.data.find({"wind.type": "N"}, {"_id": 0, "wind.type": 1, "wind.speed.rate": 1}).sort({"wind.speed.rate": 1}).limit(5))

printjson("****************************************************************");
printjson("7) find data within a rectangle and get the dewPoint (embedded - 1 layer, range)");
printjson(db.data.find({"position.coordinates.0": {$gte: 0, $lte: 0.5}, "position.coordinates.1": {$gte: 50, $lte: 55}}, {"position.coordinates": 1, "dewPoint.value": 1, _id: 0}))

printjson("****************************************************************");
printjson("8) Get section information for 3 data points that have GF1 in sections (element in array matches)");
printjson(db.data.find({sections: 'GF1'}, {_id: 0, sections: 1}).limit(3))

printjson("****************************************************************");
printjson("9) Get the past weather observation manual and atmospheric pressure change tendency code for data points with past weather observation manual containing past atmospheric condition of value 1 and quality 1 and past weather period of 6 with quality 1 (embedded object in array matches)");
printjson(db.data.find(
    {
        'pastWeatherObservationManual.atmosphericCondition': {value: '1', quality: '1'},
        'pastWeatherObservationManual.period': {value: 6, quality: '1'}
    },
    {_id: 0, pastWeatherObservationManual: 1, 'atmosphericPressureChange.tendency.code': 1}
).limit(3))

printjson("****************************************************************");
printjson("10) Get the coordinates, call letters, and elevation of data points with either the x or y or both being 69 (element in array matches)");
printjson(db.data.find({'position.coordinates': 69}, {_id: 0, 'position.coordinates': 1, callLetters: 1, elevation: 1}))
