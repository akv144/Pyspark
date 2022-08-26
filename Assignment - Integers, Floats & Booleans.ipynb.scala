// Databricks notebook source
// MAGIC %md
// MAGIC ## <u>Problem 1</u>
// MAGIC 
// MAGIC In a cricket tournament, based on the outcome of a particular match a team gets following points:
// MAGIC * <code>wins</code> gets <code>3</code> points
// MAGIC * <code>draws</code> gets <code>1</code> points
// MAGIC * <code>losses</code> gets <code>0</code> points
// MAGIC 
// MAGIC Team Aravali plays <code>8</code> matches in this tournament. It wins <code>4</code> matches, loses <code>3</code> matches and draws <code>1</code>. What is the total number of points gained by the Team Aravali?

// COMMAND ----------

// The outcome variables are defined below
var wins = 4
var losses = 3
var draws = 1

// COMMAND ----------

// # Calculate the total points gained by Team Aravali
var aravali_points =wins*3+draws*1+losses*0

// COMMAND ----------

var z=6-7

// COMMAND ----------

//aravali_points

scala.math.pow(2,2)


// COMMAND ----------

// MAGIC %md
// MAGIC ## <u>Problem 2 </u>
// MAGIC 
// MAGIC * Root of a function f(x) is defined as the value x where f(x)=0
// MAGIC * Consider a quadratic function f(x) = x^2 + 3x - 4
// MAGIC 
// MAGIC ### Find the value of the function f(x) at points   x=2,x=-1, x=1.%md

// COMMAND ----------

// # Calculate the value of the function f(x) at x = 2
func_evaluated_at_2 = 

// COMMAND ----------

// # Print the value below


// COMMAND ----------

// # Calculate the value of the function f(x) at x = -1
func_evaluated_at_minus1 = 

// COMMAND ----------

// # Print the value below


// COMMAND ----------

var apple=45;
var oranges=65;
var bananas=30;
var total=apple+oranges+bananas
var fa=(apple*100)/total
var fo=(oranges*100)/total
var fb=(bananas*100)/total

println("total"+total)

var x=bananas/total

// COMMAND ----------


	var a = 50;
	var b = 30;
	
	// Addition
	println("Addition of a + b = " + (a + b));
	
	// Subtraction
	println("Subtraction of a - b = " + (a - b));
	
	// Multiplication
	println("Multiplication of a * b = " + (a * b));
	
	// Division
	println("Division of a / b = " + ((apple)/(total));
	
	// Modulus
	println("Modulus of a % b = " + (a % b));
println(apple.getClass)



// COMMAND ----------

var v=(20/30).toString() + "."+(20%30).toString()

