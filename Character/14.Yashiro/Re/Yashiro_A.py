import variable as v;
import func.trig as trg;

function main(playerID)
{
   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);

         if (v.P_LoopMain[playerID] < 4)
         {          
            var d = 30 + 30 * v.P_LoopMain[playerID];
            var n = 4; 
            var r = 125;
            trg.Shape_Circle(playerID, 1, "50 + 1n Battlecruiser", d, n, r);
         }
         else if (v.P_LoopMain[playerID] < 8)
         {          
            var d = 30 + 30 * v.P_LoopMain[playerID];
            var n = 4; 
            var r = 125;
            trg.Shape_Circle(playerID, 1, "50 + 1n Battlecruiser", d, n, r);
            trg.Shape_Circle(playerID, 1, " Creep. Dunkelheit", d, n, r);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order(" Creep. Dunkelheit", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 8)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {      
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", playerID);

         trg.SkillEnd();
      }
   }
}