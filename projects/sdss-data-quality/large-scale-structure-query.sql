-- Massive-galaxy sample used for 3D large-scale-structure visualization
SELECT
    sp.ra,
    sp.dec,
    sp.z,
    gs.lgm_tot_p50,
    sp.specObjID
INTO mydb.Table_pr2q1
FROM SpecPhoto AS sp
JOIN galSpecExtra AS gs
  ON sp.specObjID = gs.specObjID
WHERE sp.z BETWEEN 0.05 AND 0.25
  AND gs.lgm_tot_p50 > 11
  AND sp.class = 'GALAXY'
  AND sp.ra BETWEEN 150 AND 230
  AND sp.dec BETWEEN 10 AND 50;
