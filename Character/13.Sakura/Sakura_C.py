import variable as v;
import func.trig as trg;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] < 3)
         {          
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mutalisk", 3, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 100, 0);

            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {
            trg.Shape_NxNSquare(playerID, 1, "40 + 1n Mutalisk", 3, 50);
            trg.Shape_Square(playerID, 1, "40 + 1n Mutalisk", 100, 0);

            Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, "Anywhere");
         }
         else if (v.P_LoopMain[playerID] == 7)
         {
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 8)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] < 3)
         {         
            var d = 90 + 30 * v.P_LoopMain[playerID];
            var n = 4; 
            var r = 100;
            trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r);
            trg.Shape_Circle(playerID, 1, " Unit. Hoffnung 25000", d, n, r);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 3)
         {
            trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", 90, 8, 100);
            trg.Shape_Circle(playerID, 1, "60 + 1n Hydralisk", 90, 8, 100);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "60 + 1n Hydralisk", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            Order("60 + 1n Hydralisk", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
         }
         else if (v.P_LoopMain[playerID] == 7)
         {
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", playerID);
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 8)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {      
         trg.SkillEnd();
      }
   }
}