import variable as v;
import func.trig as trg;
import func.trigadv as adv;
import func.trigepic as epic;

function Shape_X(playerID : TrgPlayer, count, unit : TrgUnit);
function Shape_X_Hallu(playerID : TrgPlayer, count, unit : TrgUnit);

function main(playerID)
{
   trg.Buff_ShieldFix(1);

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0)
         {          
            for (var i = 0; i < 2; i++)
            {
               var d = 22 + 45 * i;
               var n = 8; 
               var r = 50 + 50 * i;
               trg.Shape_Circle(playerID, 1, " Unit. Hoffnung 25000", d, n, r);
            }
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {          
            for (var i = 0; i < 2; i++)
            {
               var d = 22 + 45 * i;
               var n = 8; 
               var r = 100 + 50 * i;
               trg.Shape_Circle(playerID, 1, " Unit. Hoffnung 25000", d, n, r);
            }
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {          
            for (var i = 0; i < 4; i++)
            {
               var d = 45 * i;
               var n = 4; 
               var r = 50 + 50 * i;
               trg.Shape_Circle(playerID, 1, "40 + 1n Ghost", d, n, r);
               trg.Shape_Circle(playerID, 1, "Kakaru (Twilight)", d, n, r);
            }
            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 21)
         {                    
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);

            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] < 4)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            var d = 45;
            var n = 4; 
            var r = 25 + 25 * v.P_LoopMain[playerID];
            trg.Shape_Circle(playerID, 1, "40 + 1n Wraith", d, n, r);
            trg.Shape_Circle(playerID, 1, "40 + 1n Zealot", d, n, r);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            var d = 0;
            var size = 4; 
            var i = 64;
            trg.Shape_Cross(playerID, 1, "40 + 1n Wraith", d, size, i);
            trg.Shape_Cross(playerID, 1, " Creep. Dunkelheit", d, size, i);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 7)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 8)
         {
            var d = 0;
            var size = 4; 
            var i = 64;
            trg.Shape_Cross(playerID, 1, "Kakaru (Twilight)", d, size, i);
            trg.Shape_Cross(playerID, 1, " Unit. Hoffnung 25000", d, size, i);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 13)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] < 4)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            var d = 0;
            var n = 4; 
            var r = 25 + 25 * v.P_LoopMain[playerID];
            trg.Shape_Circle(playerID, 1, "40 + 1n Wraith", d, n, r);
            trg.Shape_Circle(playerID, 1, "40 + 1n Zealot", d, n, r);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            var d = 45;
            var size = 4; 
            var i = 64;
            trg.Shape_Cross(playerID, 1, "40 + 1n Wraith", d, size, i);
            trg.Shape_Cross(playerID, 1, " Creep. Dunkelheit", d, size, i);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 7)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 8)
         {
            var d = 0;
            var size = 4; 
            var i = 64;
            trg.Shape_Cross(playerID, 1, "Kakaru (Twilight)", d, size, i);
            trg.Shape_Cross(playerID, 1, " Unit. Hoffnung 25000", d, size, i);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 9)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 4)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            var x = 50 - 50 * v.P_LoopMain[playerID];
            var y = 100;
            trg.Shape_Square(playerID, 1, "40 + 1n Wraith", x, y);
            trg.Shape_Square(playerID, 1, "Rhynadon (Badlands)", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            trg.Shape_Edge(playerID, 1, "Bengalaas (Jungle)", 45, 5, 100);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", playerID);

            var d = 45;
            var size = 4; 
            var i = 75;
            trg.Shape_Cross(playerID, 1, "Target", d, size, i);
            KillUnitAt(All, "Target", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 6)
         {
            Shape_X(playerID, 1, "40 + 1n Guardian");

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 8)
         {
            Shape_X_Hallu(playerID, 1, "40 + 1n Wraith");
            Shape_X(playerID, 1, "Protoss Dark Templar");

            var d = 45;
            var size = 4; 
            var i = 75;
            trg.Shape_Cross(playerID, 1, "Target", d, size, i);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Wraith", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Target", "Anywhere", playerID);
            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 10)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", playerID);

            Shape_X(playerID, 1, "Kakaru (Twilight)");
            Shape_X(playerID, 1, " Unit. Hoffnung 25000");

            var d = 45;
            var size = 4; 
            var i = 75;
            trg.Shape_Cross(playerID, 1, "60 + 1n High Templar", d, size, i);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", playerID);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 12)
         {
            Shape_X(playerID, 1, "40 + 1n Ghost");

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Ghost", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         if (v.P_LoopMain[playerID] < 12 && v.P_LoopMain[playerID] % 2 == 0)
         {
            if (v.P_LoopMain[playerID] % 4 == 0)
            {
               trg.Shape_Square(playerID, 1, " Creep. Dunkelheit", 50, 50);

               MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
               MoveUnit(All, " Creep. Dunkelheit", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
               Order(" Creep. Dunkelheit", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            }

            trg.Shape_Square(playerID, 1, "Kakaru (Twilight)", 50, 50);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 16)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 4)
      {      
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}

function Shape_X(playerID : TrgPlayer, count, unit : TrgUnit)
{
   trg.Shape_Square(playerID, count, unit, -118, 182);
   trg.Shape_Square(playerID, count, unit, -68, 132);
   trg.Shape_Square(playerID, count, unit, -18, 82);
   trg.Shape_Square(playerID, count, unit, 32, 32);
   trg.Shape_Square(playerID, count, unit, 132, -68);
   trg.Shape_Square(playerID, count, unit, 182, -118);
}
function Shape_X_Hallu(playerID : TrgPlayer, count, unit : TrgUnit)
{
   epic.Shape_Square(playerID, count, unit, -118, 182, 1);
   epic.Shape_Square(playerID, count, unit, -68, 132, 1);
   epic.Shape_Square(playerID, count, unit, -18, 82, 1);
   epic.Shape_Square(playerID, count, unit, 32, 32, 1);
   epic.Shape_Square(playerID, count, unit, 132, -68, 1);
   epic.Shape_Square(playerID, count, unit, 182, -118, 1);
}