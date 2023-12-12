CREATE TABLE telecom.telecom (
       BearerId varchar, Start_time varchar, Start_ms varchar, End_time varchar, End_ms varchar, Dur_ms varchar, IMSI varchar,
       MSISDN_number varchar, IMEI varchar, LastLocationName varchar, AvgRTTDL_ms varchar,
       AvgRTTUL_ms varchar, AvgBearerTPDL_kbps varchar, AvgBearerTPUL_kbps varchar,
       TCPDLRetransVol_Bytes varchar, TCPULRetransVol_Bytes varchar,
       DLTPless50Kbps varchar, 50KbpslessDLTPless250Kbps varchar,
       250Kbps<DLTP<1Mbps(%) varchar, DLTP>1Mbps(%) varchar,
       ULTP<10Kbps(%) varchar, 10Kbps<ULTP<50Kbps(%) varchar,
       50Kbps<ULTP<300Kbps(%) varchar, ULTP>300Kbps(%) varchar,
       HTTPDL(Bytes) varchar, HTTPUL(Bytes) varchar, ActivityDurationDL(ms) varchar,
       ActivityDurationUL(ms) varchar, Dur(ms)1 varchar, HandsetManufacturer varchar,
       HandsetType varchar, Nbofsecwith125000B<VolDL varchar,
       Nbofsecwith1250B<VolUL<6250B varchar,
       Nbofsecwith31250B<VolDL<125000B varchar,
       Nbofsecwith37500B<VolUL varchar,
       Nbofsecwith6250B<VolDL<31250B varchar,
       Nbofsecwith6250B<VolUL<37500B varchar,
       NbofsecwithVolDL<6250B varchar, NbofsecwithVolUL<1250B varchar,
       SocialMediaDL(Bytes) varchar, SocialMediaUL(Bytes) varchar,
       GoogleDL(Bytes) varchar, GoogleUL(Bytes) varchar, EmailDL(Bytes) varchar,
       EmailUL(Bytes) varchar, YoutubeDL(Bytes) varchar, YoutubeUL(Bytes) varchar,
       NetflixDL(Bytes) varchar, NetflixUL(Bytes) varchar, GamingDL(Bytes) varchar,
       GamingUL(Bytes) varchar, OtherDL(Bytes) varchar, OtherUL(Bytes) varchar,
       TotalUL(Bytes) varchar, TotalDL(Bytes) varchar
);


COPY telecom.customers (first_name, last_name, email, phone_number)
FROM 'C:\Users\YourUsername\Downloads\telecom.csv'
DELIMITER ',' CSV HEADER;
