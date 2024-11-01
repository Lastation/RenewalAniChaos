import variable as v;
import func.trig as trg;
import func.trigadv as adv;

function main(playerID)
{
   trg.Debuff_Stop();
   trg.Debuff_BanReturn();

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 45, 4, 75);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 1)
         {
            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 45, 6, 150);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);

            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 45, 4, 75);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);            
         }
         else if (v.P_LoopMain[playerID] == 2)
         {
            adv.Shape_QuadNxNSquareAt(playerID, 1, "50 + 1n Battlecruiser", 2, 75, 150, 150);
            adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n Siege", 2, 75, 150, 150);

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         } 

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 13)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            trg.Shape_Edge(playerID, 1, "60 + 1n Danimoth", 0, 7, 150);
            trg.Shape_Edge(playerID, 1, "60 + 1n Archon", 0, 7, 150);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("60 + 1n Danimoth", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 2)
         {
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         } 
  
         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 13)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            adv.Shape_QuadNxNSquareAt(playerID, 1, "40 + 1n Mojo", 2, 50, 75, 75);
            adv.Shape_QuadNxNSquareAt(playerID, 1, "60 + 1n Archon", 2, 50, 75, 75);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("40 + 1n Mojo", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            adv.Shape_QuadNxNSquareAt(playerID, 1, "Kakaru (Twilight)", 3, 50, 150, 150);
            adv.Shape_QuadNxNSquareAt(playerID, 1, " Unit. Hoffnung 25000", 3, 50, 150, 150);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", playerID);
         }
         else if (v.P_LoopMain[playerID] == 4)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", playerID);
         } 

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 6)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);

         trg.SkillEnd();      
      }
   }
}