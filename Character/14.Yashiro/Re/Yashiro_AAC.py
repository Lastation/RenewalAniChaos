import variable as v;
import func.trig as trg;

function main(playerID)
{
   if (v.P_CountMain[playerID] >= 2)
   {
      trg.Buff_ShieldFix(1);
   }

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 2)
         {          
            var d = 225;
            var n = 4; 
            var interval = 100;
            var distance = interval * 3 / 2 - interval * v.P_LoopMain[playerID];
            trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", d, n, interval, distance);
            trg.Shape_Line(playerID, 1, "60 + 1n Archon", d, n, interval, distance);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] < 4)
         {
            var d = 45;
            var n = 4; 
            var interval = 100;
            var distance = interval / 2 + interval * (v.P_LoopMain[playerID] - 2);
            trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", d, n, interval, distance);
            trg.Shape_Line(playerID, 1, "60 + 1n Archon", d, n, interval, distance);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 5)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 2)
         {          
            var d = 315;
            var n = 4; 
            var interval = 75;
            var distance = interval * 3 / 2 - interval * v.P_LoopMain[playerID];
            trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", d, n, interval, distance);
            trg.Shape_Line(playerID, 1, "60 + 1n Archon", d, n, interval, distance);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] < 4)
         {
            var d = 135;
            var n = 4; 
            var interval = 75;
            var distance = interval / 2 + interval * (v.P_LoopMain[playerID] - 2);
            trg.Shape_Line(playerID, 1, "50 + 1n Battlecruiser", d, n, interval, distance);
            trg.Shape_Line(playerID, 1, "60 + 1n Archon", d, n, interval, distance);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 5)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] == 0)
         {          
            trg.Shape_NxNSquare(playerID, 1, "50 + 1n Battlecruiser", 4, 125);
            trg.Shape_NxNSquare(playerID, 1, "60 + 1n Archon", 4, 125);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {          
            trg.Shape_NxNSquare(playerID, 1, "Kakaru (Twilight)", 4, 125);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 12)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 8)
         {          
            var d = 22 + 90 * v.P_LoopMain[playerID];
            var n = 8; 
            var interval = 64;
            var distance = 120;
            trg.Shape_Line(playerID, 1, "40 + 1n Mojo", d, n, interval, distance);
            n = 6;
            trg.Shape_Line(playerID, 1, " Creep. Dunkelheit", d, n, interval, distance);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order(" Creep. Dunkelheit", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
         }
         if (v.P_LoopMain[playerID] < 9 && v.P_LoopMain[playerID] > 0)
         {          
            var d = 22 + 270 + 90 * v.P_LoopMain[playerID];
            var n = 8; 
            var interval = 64;
            var distance = 120;
            trg.Shape_Line(playerID, 1, "Kakaru (Twilight)", d, n, interval, distance);
            trg.Shape_Line(playerID, 1, "60 + 1n Archon", d, n, interval, distance);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 9)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 4)
      {      
         trg.SkillEnd();
      }
   }
}