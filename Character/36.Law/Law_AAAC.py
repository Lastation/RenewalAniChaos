import variable as v;
import func.trig as trg;
import func.trigepic as epic;
import func.trigadv as adv;
import func.sound as s;

var x = 0;
var y = 0;

var d = 0;

function Shape_X(playerID : TrgPlayer, count, unit : TrgUnit);
function Shape_Dia(playerID : TrgPlayer, count, unit : TrgUnit);
function Shape_DoubleX(playerID : TrgPlayer, count, unit : TrgUnit);

function main(playerID)
{
   trg.Debuff_BanReturn();
   if (v.P_CountMain[playerID] <= 2 && v.P_LoopMain[playerID] % 2 == 0)
   {
      MoveUnit(All, "80 + 1n Artanis", playerID, "Anywhere", "[Skill]HoldPosition");
   }
   MoveUnit(All, "60 + 1n Archon", playerID, "Anywhere", "[Skill]HoldPosition");
   KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            Shape_X(playerID, 1, "40 + 1n Mojo");
            Shape_X(playerID, 1, "60 + 1n Archon");

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            Shape_X(playerID, 1, "60 + 1n High Templar");
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            Shape_X(playerID, 1, "Kakaru (Twilight)");
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         } 

         var d = 23 * v.P_LoopMain[playerID];
         var distance = 50 + 50 * (v.P_LoopMain[playerID] % 5);

         trg.Table_Sin(playerID, d, distance);
         trg.Table_Cos(playerID, d, distance);
         
         var x = v.P_AngleCos[playerID];
         var y = v.P_AngleSin[playerID];

         adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n High Templar", 2, 50, x, y);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 46)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            Shape_Dia(playerID, 1, "40 + 1n Mojo");
            Shape_Dia(playerID, 1, "60 + 1n Archon");

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            Shape_Dia(playerID, 1, "60 + 1n Archon");

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n Archon", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("60 + 1n Archon", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            Shape_Dia(playerID, 1, "Kakaru (Twilight)");
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         } 

         var d = 23 * v.P_LoopMain[playerID];
         var distance = 50 + 50 * (v.P_LoopMain[playerID] % 5);

         trg.Table_Sin(playerID, d, distance);
         trg.Table_Cos(playerID, d, distance);
         
         var x = v.P_AngleCos[playerID];
         var y = v.P_AngleSin[playerID];

         adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n High Templar", 2, 50, x, y);

         if (v.P_LoopMain[playerID] % 5 == 4)
         {
            trg.Shape_Square(playerID, 1, "80 + 1n Artanis", x, y);
         } 
         MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
         Order("80 + 1n Artanis", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 27)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 8) 
         {
            trg.Shape_Cross(playerID, 1, "40 + 1n Wraith", 45, v.P_LoopMain[playerID] + 1, 50);
            trg.Shape_Cross(playerID, 1, "60 + 1n High Templar", 45, v.P_LoopMain[playerID] + 1, 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] < 18)
         {
            trg.Shape_Cross(playerID, 1, "40 + 1n Wraith", 45, 8, 50);
            trg.Shape_Cross(playerID, 1, "60 + 1n High Templar", 45, 8, 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] < 27)
         {
            Shape_DoubleX(playerID, 1, "40 + 1n Wraith");
            Shape_DoubleX(playerID, 1, "60 + 1n High Templar");

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         } 
         else if (v.P_LoopMain[playerID] == 28)
         {
            Shape_DoubleX(playerID, 1, "40 + 1n Wraith");
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 34)
         {
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mojo", 11, 50);
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Archon", 11, 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 36)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "60 + 1n High Templar", 11, 50);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 38)
         {
            trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 11, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         var d = 23 * v.P_LoopMain[playerID];
         var distance = 50 + 50 * (v.P_LoopMain[playerID] % 5);

         trg.Table_Sin(playerID, d, distance);
         trg.Table_Cos(playerID, d, distance);
         
         var x = v.P_AngleCos[playerID];
         var y = v.P_AngleSin[playerID];

         adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n High Templar", 2, 50, x, y);

         if (v.P_LoopMain[playerID] % 5 == 4)
         {
            trg.Shape_Square(playerID, 1, "80 + 1n Artanis", x, y);
         } 
         MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
         Order("80 + 1n Artanis", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 80)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         if (v.P_LoopMain[playerID] < 8)
         {
            trg.Shape_NxNSquare(playerID, 1, "Rhynadon (Badlands)", 4 + v.P_LoopMain[playerID], 50);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", playerID);
         }      
         else if (v.P_LoopMain[playerID] == 8)
         {
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Wraith", 3, 50);
            trg.Shape_NxNSquare(playerID, 1, "Bengalaas (Jungle)", 3, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID);
         }      
         else if (v.P_LoopMain[playerID] == 9)
         {
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Wraith", 7, 50);
            trg.Shape_NxNSquare(playerID, 1, "Bengalaas (Jungle)", 7, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID);
         }      
         else if (v.P_LoopMain[playerID] == 10)
         {
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Wraith", 11, 50);
            trg.Shape_NxNSquare(playerID, 1, "Bengalaas (Jungle)", 11, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID);
         }             
         else if (v.P_LoopMain[playerID] == 11)
         {
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Guardian", 11, 50);
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Archon", 11, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }    
         else if (v.P_LoopMain[playerID] == 12)
         {
            trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 11, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }    


         var d = 3 * v.P_LoopMain[playerID];
         var distance = 50 + 50 * (v.P_LoopMain[playerID] % 5);

         trg.Table_Sin(playerID, d, distance);
         trg.Table_Cos(playerID, d, distance);
         
         var x = v.P_AngleCos[playerID];
         var y = v.P_AngleSin[playerID];

         adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n High Templar", 3, 50, x, y);

         if (v.P_LoopMain[playerID] % 5 == 4)
         {
            trg.Shape_Square(playerID, 1, "80 + 1n Artanis", x, y);
         } 
         MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
         Order("80 + 1n Artanis", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 20)
         {                        
            KillUnitAt(All, "80 + 1n Artanis", "Anywhere", playerID);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 4)
      {
         if (v.P_LoopMain[playerID] < 20)
         {
            RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);

            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mojo", 11, 50);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            if (v.P_LoopMain[playerID] % 2 == 0)
            {
               trg.Shape_NxNSquare(playerID, 1, "60 + 1n Archon", 11, 50);
            }
            else
            {
               trg.Shape_NxNSquare(playerID, 1, "60 + 1n High Templar", 11, 50);
            }
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
         }      

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 24)
         {                        
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
            
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }

      else if (v.P_CountMain[playerID] == 5)
      {
         trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 11, 50);
         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);

         SetSwitch("UiltimateSwitch", Clear);
         trg.SkillEnd();
      }
   }
}

function Shape_X(playerID : TrgPlayer, count, unit : TrgUnit)
{
   var interval = 32;
   var n = 9;
   var x_o = 2 * interval;
   var y_o = 0;

   var x_i = interval;
   var y_i = interval;

   trg.Shape_Dot(playerID, count, unit, 0, 0);

   for (var i = 0; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o + i * x_i, y_o + i * x_i);
   }

   x_o -= interval;
   y_o += interval;

   for (var i = 0; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o + i * x_i, y_o + i * x_i);
   }

   x_o -= interval;
   y_o += interval;

   for (var i = 1; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o + i * x_i, y_o + i * x_i);
   }
}

function Shape_DoubleX(playerID : TrgPlayer, count, unit : TrgUnit)
{
   var interval = 32;
   var n = 7;
   var x_o = interval;
   var y_o = 0;

   var x_i = interval;
   var y_i = interval;

   for (var i = 0; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o + i * x_i, y_o + i * x_i);
   }

   x_o -= interval;
   y_o += interval;

   for (var i = 1; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o + i * x_i, y_o + i * x_i);
   }
}

function Shape_Dia(playerID : TrgPlayer, count, unit : TrgUnit)
{
   var interval = 64;
   var n = 6;
   var x_o = interval * 10 / 14 * (n + 2);
   var y_o = 0;

   var x_i = interval;
   var y_i = interval;

   for (var i = 0; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o - i * x_i, y_o + i * x_i);
   }

   x_o -= interval;
   y_o -= interval;

   for (var i = 0; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o - i * x_i, y_o + i * x_i);
   }

   x_o -= interval;
   y_o -= interval;

   for (var i = 1; i < n; i++)
   {
      trg.Shape_Square(playerID, count, unit, x_o - i * x_i, y_o + i * x_i);
   }
}