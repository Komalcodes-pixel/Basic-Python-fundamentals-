import pandas as pd
file = input("Enter the file name or its path")
df = pd.read_csv(file)

print("Student Data:")
print(df)
avg_marks = df["Marks"].mean()
print("\nAverage Marks:", avg_marks)
topper = df.loc[df["Marks"].idxmax()]
print("\nTopper Details:")
print(topper)
passed_students = df[df["Marks"] >= 40].shape[0]
print("\nNumber of Passed Students:", passed_students)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(grade)
print("\nFinal Data with Result & Grade:")
print(df)
# Save final result:
final = input("Enter the file to save the result")
df.to_csv(final, index=False)
print("\nFinal result saved to final_result.csv")





