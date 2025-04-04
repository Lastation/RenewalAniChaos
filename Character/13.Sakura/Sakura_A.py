import variable as v;
import func.trig as trg;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 4)
         {          
            trg.Shape_Dot(playerID, 1, "40 + 1n Mutalisk", 0, 0);

            Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, "Anywhere");

            var d = 90 + 90 * v.P_LoopMain[playerID] / 4;
            var n = 4; 
            var r = 100;
            trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r);
            trg.Shape_Circle(playerID, 1, " Unit. Hoffnung 25000", d, n, r);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 4)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 4)
         {          
            trg.Shape_Dot(playerID, 1, "40 + 1n Mutalisk", 0, 0);

            Order("40 + 1n Mutalisk", playerID, "Anywhere", Attack, "Anywhere");

            var d = 90 + 90 * v.P_LoopMain[playerID] / 4;
            var n = 4; 
            var r = 100;
            trg.Shape_Circle(playerID, 1, "40 + 1n Guardian", d, n, r);
            trg.Shape_Circle(playerID, 1, "Protoss Dark Archon", d, n, r);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Guardian", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 4)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {      
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", playerID);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
         trg.SkillEnd();
      }
   }
}