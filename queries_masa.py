import numpy as np
import sqlite3
import matplotlib.pyplot as plt


db_file = './db/fy2019.db'
db = sqlite3.connect(db_file)
cursor = db.cursor()


# Average num_floors for each LU
# Average value for year built
# Average value for sq feet in 3 categories

LU_LIST = ["A", "E", "AH", "EA", "C", "I", "CC", "R1", "CD", "R2", "CL", "R3", "CM", "R4", "R4", "RC", "CP", "RL"]
YR_BUILT_LIST = [(float('-inf'), 18.5), (18.5, 54.5), (54.5, 79.5), (79.5, 98.5), (98.5, 104.5), (104.5, 113.5), (113.5, 118.5),(118.5, 119.5), (119.5, 129.5), (129.5, float('inf'))]
LAND_SF_LIST = [(float('-inf'),211148788.5),(211148788.5, 422277612),(422277612,633406435.5),(633406435.5, 844535259), (844535259, 1055664082.5), (1055664082.5,1266792906), (1266792906,1477921729.5), (1477921729.5,1689050553),(1689050553,1900179376.5),(1900179376.5,float('inf'))]
OCC_LIST = ["Y", "N"]

# Average num_floors for each LU
avg_num_floor_lu = {}
for LU in LU_LIST:
    command = "SELECT AVG(NUM_FLOORS) FROM fy19_transformed WHERE LU = ?;"
    cursor.execute(command, [LU])
    for row in cursor:
        avg_num_floor_lu[LU] = row[0]

print("avg_num_floor_lu:\t", avg_num_floor_lu)

# lists = sorted(avg_num_floor_lu.items()) # sorted by key, return a list of tuples

x = [round(v, 2) if isinstance(v, float) else v for v in avg_num_floor_lu.keys()]
y = [0 if v is None else v for v in avg_num_floor_lu.values()]
y_pos = np.arange(len(x))
plt.figure(figsize=(10,5))
plt.bar(y_pos, y, align='center', alpha=0.5)
plt.xticks(y_pos, x)
plt.ylabel('Usage')
plt.title('Average Number of Floors')
plt.show()


# Average value for year built
avg_val_yb = {}
for YR_BUILT in YR_BUILT_LIST:
    command = "SELECT AVG(AV_TOTAL) FROM fy19_transformed WHERE YR_BUILT > ? AND YR_BUILT <= ?;"
    cursor.execute(command, [YR_BUILT[0],YR_BUILT[1]])
    for row in cursor:
        avg_val_yb[YR_BUILT] = row[0]

print("avg_val_yb:\t", avg_val_yb)


# x = avg_val_yb.keys()
x = [round(v, 2) if isinstance(v, float) else v for v in avg_val_yb.keys()]
y = [0 if v is None else v for v in avg_val_yb.values()]
y_pos = np.arange(len(x))
plt.figure(figsize=(10,5))
plt.bar(y_pos, y, align='center', alpha=0.5)
plt.xticks(y_pos, x)
plt.ylabel('Usage')
plt.title('Average Value for Year Built')

plt.show()




# Average value for sq feet in 3 categories

avg_val_ls = {}
for LAND_SF in LAND_SF_LIST:
    command = "SELECT AVG(AV_TOTAL) FROM fy19_transformed WHERE LAND_SF > ? AND LAND_SF <= ?;"
    cursor.execute(command, [LAND_SF[0],LAND_SF[1]])
    for row in cursor:
        avg_val_ls[LAND_SF] = row[0]
print("avg_val_ls:\t", avg_val_ls)

# x = avg_val_ls.keys()
x = [round(v, 2) if isinstance(v, float) else v for v in avg_val_ls.keys()]
y = [0 if v is None else v for v in avg_val_ls.values()]
y_pos = np.arange(len(x))
plt.figure(figsize=(10,5))
plt.bar(y_pos, y, align='center', alpha=0.5)
plt.xticks(y_pos, x)
plt.ylabel('Usage')
plt.title('Average Value for SQ Feet')

plt.show()

# Average value for sq feet by OWN OCC

avg_val_occ = {}
for OCC in OCC_LIST:
    command = "SELECT AVG(AV_TOTAL) FROM fy19_transformed WHERE OWN_OCC = ?;"
    cursor.execute(command, [OCC])
    for row in cursor:
        avg_val_occ[OCC] = row[0]
print("avg_val_occ:\t", avg_val_occ)

# x = avg_val_occ.keys()
x = [round(v, 2) if isinstance(v, float) else v for v in avg_val_occ.keys()]
y = [0 if v is None else v for v in avg_val_occ.values()]
y_pos = np.arange(len(x))
plt.figure(figsize=(10,5))
plt.bar(y_pos, y, align='center', alpha=0.5)
plt.xticks(y_pos, x)
plt.ylabel('Usage')
plt.title('Average Value for Owned OCC')

plt.show()



db.commit()
db.close()

