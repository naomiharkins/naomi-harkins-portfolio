-- SDSS galaxy sample used to evaluate spectroscopic completeness
SELECT
    ra,
    dec,
    petroMag_r,
    modelMag_g,
    modelMag_r,
    extinction_g,
    extinction_r,
    petroR50_r,
    specObjID
INTO mydb.MyTable_p1q2
FROM Galaxy
WHERE ra BETWEEN 150 AND 230
  AND dec BETWEEN 10 AND 50
  AND psfMag_r - cModelMag_r > 0.24
  AND petroMag_r - extinction_r < 17.5
  AND clean = 1;
