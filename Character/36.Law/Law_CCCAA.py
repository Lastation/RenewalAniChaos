import variable as v;
import func.trig as trg;
import func.trigadv as adv;

function main(playerID)
{
   trg.Debuff_Stop();
   trg.Debuff_BanReturn();

   var x;
   var y;

   if (v.P_WaitMain[playerID] == 0)
   {
      if (v.P_CountMain[playerID] == 0)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            trg.Shape_Edge(playerID, 1, "40 + 1n Guardian", 45, 5, 100);
            trg.Shape_Edge(playerID, 1, "Protoss Dark Archon", 45, 4, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", playerID);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);

            trg.Shape_Edge(playerID, 1, "50 + 1n Tank", 45, 4, 100);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", playerID, "[Skill]Unit_Wait_ALL", v.P_LocationID[playerID]);
            Order("50 + 1n Tank", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);  
         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 18)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 1)
      {
         if (v.P_LoopMain[playerID] == 0) 
         {
            trg.Shape_Edge(playerID, 1, "60 + 1n Siege", 45, 6, 200);

            trg.Shape_Edge(playerID, 1, "50 + 1n Battlecruiser", 45, 7, 200);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);

         }

         trg.Main_Wait(80);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 25)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 2)
      {
         if (v.P_LoopMain[playerID] < 6) 
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);

            trg.Table_Sin(playerID, 22 + 22 * v.P_LoopMain[playerID], 125);
            trg.Table_Cos(playerID, 22 + 22 * v.P_LoopMain[playerID], 125);

            x = v.P_AngleCos[playerID];
            y = v.P_AngleSin[playerID];

            trg.Shape_Square(playerID, 1, "50 + 1n Battlecruiser", x, y);
            trg.Shape_Square(playerID, 1, "60 + 1n Danimoth", x, y);
            trg.Shape_Square(playerID, 1, " Unit. Hoffnung 25000", x, y);
            trg.Shape_Square(playerID, 1, "Protoss Dark Archon", x, y);

            MoveLocation(v.P_LocationID[playerID], v.P_UnitID[playerID], playerID, "Anywhere");
            Order("50 + 1n Battlecruiser", playerID, "Anywhere", Attack, v.P_LocationID[playerID]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", playerID);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", playerID);
         }

         trg.Main_Wait(160);

         v.P_LoopMain[playerID] += 1;

         if (v.P_LoopMain[playerID] == 6)
         {                        
            v.P_CountMain[playerID] += 1;
            v.P_LoopMain[playerID] = 0;
         }
      }
      else if (v.P_CountMain[playerID] == 3)
      {
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", playerID);
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", playerID);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", playerID);

         trg.SkillEnd();      
      }
   }
}